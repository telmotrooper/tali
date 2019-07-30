#!/usr/bin/env python3

import os
from func.get_ram_amount import get_ram_amount
from func.disk_utils import select_disk
from func.get_firmware_interface import get_firmware_interface

ram = get_ram_amount()

print(f"We detected {ram} MiB of RAM, a swap partition is gonna be created with this size.".format(ram))

swap_end_bios = 101 + int(ram)
swap_end_uefi = 261 + int(ram)

print("Which disk should be partitioned? ")
disk = select_disk()

fw_interface = get_firmware_interface()

if(fw_interface == "BIOS"):
  os.system(f"""
    parted --script {disk} \
    mklabel msdos \
    mkpart primary ext4 1MiB 101MiB \
    set 1 boot on \
    mkpart primary linux-swap 101MiB {swap_end_bios}MiB \
    mkpart primary ext4 {swap_end_bios}MiB 100%""")

else: # UEFI
  os.system(f"""
    parted --script {disk} \
    mklabel gpt \
    mkpart primary fat32 1MiB 261MiB \
    set 1 esp on \
    mkpart primary linux-swap 261MiB {swap_end_uefi}MiB \
    mkpart primary ext4 {swap_end_uefi}MiB 100%""")


print("--- Formatting partitions ---")
if(fw_interface == "BIOS"):
  os.system("mkfs.ext4 /dev/sda1")
else: # UEFI
  os.system("mkfs.fat -F32 /dev/sda1")

os.system("mkswap /dev/sda2")
os.system("swapon /dev/sda2")
os.system("mkfs.ext4 /dev/sda3")

print("--- Mounting partitions ---")
os.system("mount /dev/sda3 /mnt")
os.system("mkdir /mnt/boot")
os.system("mount /dev/sda1 /mnt/boot")
