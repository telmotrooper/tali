#!/usr/bin/env python3

print("We're assuming you've set your partitions by now and properly mounted on /mnt")

import os

os.system("pacstrap /mnt base")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("arch-chroot /mnt")
