#!/usr/bin/env python3

import os
import argparse
from utils.get_ram_amount import get_ram_amount
from utils.disk_utils import select_disk
from utils.get_firmware_interface import get_firmware_interface
from utils.colors import cyan, green, yellow
from utils.yes_no_dialog import yes_no_dialog

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--debug")
  args = parser.parse_args()

  print(args)

  ram = get_ram_amount()

  print("Which disk should be partitioned? ")
  disk = select_disk()

  suffix = "p" if ("nvme" in disk) else "" # NVMe numbers partitions as p1, p2, p3 instead of 1, 2, 3.

  use_swap = yes_no_dialog(f"We detected {ram} MiB of RAM, should we create a swap partition of the same size?")

  fw_interface = get_firmware_interface()

  # Boot partition size (MiB)
  boot_bios = 261
  boot_uefi = 261
  boot_size = boot_uefi if fw_interface == "UEFI" else boot_bios

  swap_end = int(ram) + boot_size

  parted_command = ""

  if(fw_interface == "BIOS"):
    if(use_swap):
      parted_command = f"""
        parted --script {disk} \
        mklabel msdos \
        mkpart primary ext4 1MiB {boot_size}MiB \
        set 1 boot on \
        mkpart primary linux-swap {boot_size}MiB {swap_end}MiB \
        mkpart primary ext4 {swap_end}MiB 100%"""
    else:
      parted_command = f"""
        parted --script {disk} \
        mklabel msdos \
        mkpart primary ext4 1MiB {boot_size}MiB \
        set 1 boot on \
        mkpart primary ext4 {boot_size}MiB 100%"""

  else: # UEFI
    if(use_swap):
      parted_command = f"""
        parted --script {disk} \
        mklabel gpt \
        mkpart primary fat32 1MiB {boot_size}MiB \
        set 1 esp on \
        mkpart primary linux-swap {boot_size}MiB {swap_end}MiB \
        mkpart primary ext4 {swap_end}MiB 100%"""
    else:
      parted_command = f"""
        parted --script {disk} \
        mklabel gpt \
        mkpart primary fat32 1MiB {boot_size}MiB \
        set 1 esp on \
        mkpart primary ext4 {boot_size}MiB 100%"""

  os.system(parted_command)

  print("--- Formatting partitions ---")
  if(fw_interface == "BIOS"):
    os.system(f"mkfs.ext4 {disk}{suffix}1")
  else: # UEFI
    os.system(f"mkfs.fat -F32 {disk}{suffix}1")

  if(use_swap):
    os.system(f"mkswap {disk}{suffix}2")
    os.system(f"swapon {disk}{suffix}2")
    os.system(f"mkfs.ext4 {disk}{suffix}3")
    print("--- Mounting partitions ---")
    os.system(f"mount {disk}{suffix}3 /mnt")
  else:
    os.system(f"mkfs.ext4 {disk}{suffix}2")
    print("--- Mounting partitions ---")
    os.system(f"mount {disk}{suffix}2 /mnt")

  # These steps are the same for all combinations
  os.system(f"mkdir /mnt/boot")
  os.system(f"mount {disk}{suffix}1 /mnt/boot")

  print("You're all set, run " + green("tali/install.py") + " to continue installing " + cyan("Arch Linux") + ".")

if __name__ == "__main__":
  main()
