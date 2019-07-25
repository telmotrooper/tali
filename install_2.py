#!/usr/bin/env python3

input("Did you set your partitions, format them and mount them on /mnt?")

import os

os.system("pacstrap /mnt base base-devel net-tools xdg-user-dirs")
os.system("pacstrap /mnt python wget")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("cp install_3.py /mnt")
os.system("cp set_themes_and_kb_layout.py /mnt")
os.system("arch-chroot /mnt python install_3.py")
