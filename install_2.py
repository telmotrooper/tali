#!/usr/bin/env python3

print("We're assuming you've set your partitions, formated them by now they're properly mounted on /mnt")

import os

os.system("pacstrap /mnt base")
os.system("pacstrap /mnt python wget")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("arch-chroot /mnt")
