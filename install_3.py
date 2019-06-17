#!/usr/bin/env python3

import os

os.system("ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime")
os.system("hwclock --systohc")
os.system("cat /etc/locale.gen | sed 's/#en_US.UTF-8/en_US.UTF-8/g' > /locale.gen")
os.system("mv /locale.gen /etc/")
os.system("locale-gen")
os.system("echo 'LANG=en_US.UTF-8' > /etc/locale.conf")
os.system("echo 'KEYMAP=br-abnt2' > /etc/vconsole.conf")

hostname = input("Set your computer's name: ")
os.system("echo '{}' > /etc/hostname".format(hostname))
os.system("pacman -S --noconfirm ttf-bitstream-vera grub gdm cinnamon gnome-terminal firefox gnome-system-monitor")
os.system("systemctl enable gdm")
os.system("systemctl enable NetworkManager")
print("Set the root password: ")
os.system("passwd")
username = input("Set your username: ")
os.system("useradd -m -G wheel -s /bin/bash {}".format(username))
print("Set the password for {}".format(username))
os.system("passwd {}".format(username))
os.system("cat /etc/sudoers | sed 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' > /etc/sudoers_new")
os.system("mv /etc/sudoers_new /etc/sudoers")

