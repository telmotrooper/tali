#!/usr/bin/env python3

import os, subprocess

ram = subprocess.check_output(
  "free -m | grep Mem | awk '{print $2}'",
  shell=True, stderr=subprocess.STDOUT).decode().rstrip()

print("We detected {} MiB of RAM, a swap partition is gonna be created with this size.".format(ram))

swap_end = 101 + int(ram)

print("The disks available are: ")
os.system("fdisk -l | grep 'Disk /' | awk '{print $2, $3, $4}'")
disk = input("Which disk should be partitioned? ")
os.system(f"""
  parted --script {disk} \
  mklabel msdos \
  mkpart primary 1MiB 101MiB \
  set 1 boot on \
  mkpart primary linux-swap 101MiB {swap_end} \
  mkpart primary 101MiB 100%""")

print("--- Formatting partitions ---")
os.system("mkfs.ext4 /dev/sda1")
os.system("mkswap /dev/sda2")
os.system("swapon /dev/sda2")
os.system("mkfs.ext4 /dev/sda3")

print("--- Mounting partitions ---")
os.system("mount /dev/sda2 /mnt")
os.system("mkdir /mnt/boot")
os.system("mount /dev/sda1 /mnt/boot")
