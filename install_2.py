#!/usr/bin/env python3

input("Did you set your partitions, format them and mount them on /mnt?")

import os

os.system("pacstrap /mnt base")
os.system("pacstrap /mnt python wget")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("cp /root/install_3.py /mnt")
os.system("arch-chroot /mnt")
