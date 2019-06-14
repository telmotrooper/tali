#!/usr/bin/env python3

import os

os.system("ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime")
os.system("hwclock --systohc")
os.system("cat /etc/locale.gen | sed 's/#en_US.UTF-8/en_US.UTF-8/g' > /locale.gen")
os.system("mv /locale.gen /etc/")
os.system("locale-gen")
os.system("echo 'LANG=en_US.UTF-8' > /etc/locale.conf")
os.system("echo 'KEYMAP=br-abnt2' > /etc/vconsole.conf")

hostname = input("What should be this computer's name?")
os.system("echo '{}' > /etc/hostname".format(hostname))
os.system("pacman -S ttf-bitstream-vera gdm cinnamon")
os.system("systemctl enable gdm")

# gotta set root password yet