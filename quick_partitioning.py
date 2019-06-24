#!/usr/bin/env python3

import os

print("The disks available are: ")
os.system("fdisk -l | grep 'Disk /' | awk '{print $2, $3, $4}'")
disk = input("Which disk should be partitioned? ")
os.system("parted --script {} \ mklabel msdos \ mkpart primary 1MiB 101MiB \ set 1 boot on \ mkpart primary 101MiB 100%".format(disk))

print("--- Formatting partitions ---")
os.system("mkfs.ext4 /dev/sda1")
os.system("mkfs.ext4 /dev/sda2")

print("--- Mounting partitions ---")
os.system("mount /dev/sda2 /mnt")
os.system("mkdir /mnt/boot")
os.system("mount /dev/sda1 /mnt/boot")
