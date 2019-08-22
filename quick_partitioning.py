#!/usr/bin/env python3

import os
from func.get_ram_amount import get_ram_amount
from func.disk_utils import select_disk
from func.get_firmware_interface import get_firmware_interface

ram = get_ram_amount()

print(f"We detected {ram} MiB of RAM, a swap partition is gonna be created with this size.")

print("Which disk should be partitioned? ")
disk = select_disk()

fw_interface = get_firmware_interface()

swap_end = int(ram)

if(fw_interface == "BIOS"):
  swap_end += 101 # 100 MiB
else: #UEFI
  swap_end += 261 # 260 MiB

if(fw_interface == "BIOS"):
  os.system(f"""
    parted --script {disk} \
    mklabel msdos \
    mkpart primary ext4 1MiB 101MiB \
    set 1 boot on \
    mkpart primary linux-swap 101MiB {swap_end}MiB \
    mkpart primary ext4 {swap_end}MiB 100%""")

else: # UEFI
  os.system(f"""
    parted --script {disk} \
    mklabel gpt \
    mkpart primary fat32 1MiB 261MiB \
    set 1 esp on \
    mkpart primary linux-swap 261MiB {swap_end}MiB \
    mkpart primary ext4 {swap_end}MiB 100%""")


print("--- Formatting partitions ---")
if(fw_interface == "BIOS"):
  os.system(f"mkfs.ext4 {disk}1")
else: # UEFI
  os.system(f"mkfs.fat -F32 {disk}1")

os.system(f"mkswap {disk}2")
os.system(f"swapon {disk}2")
os.system(f"mkfs.ext4 {disk}3")

print("--- Mounting partitions ---")
os.system(f"mount {disk}3 /mnt")
os.system(f"mkdir /mnt/boot")
os.system(f"mount {disk}1 /mnt/boot")
