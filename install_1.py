#!/usr/bin/env python3

import os, re
from func.get_firmware_interface import get_firmware_interface
from func.get_wireless_devices import get_wireless_devices

# ANSI escape codes for formatting in the terminal
cyan = "\u001b[36m"
reset = "\u001b[0m"

print(cyan + "TALI (Telmo's Arch Linux Installer)\n" + reset)

wl_devices = get_wireless_devices()

if(wl_devices != []): # at least one wireless device was found
  print("The following Wi-Fi devices were found:")
  for device in wl_devices:
    print(device)
else:
  print("No Wi-Fi device found.")

print(f"\nYou're running {get_firmware_interface()}")

os.system("fdisk -l | grep 'Disk /' | awk '{print $2, $3, $4}'")

print("Setting keyboard layout to 'br-abnt2'")
os.system("loadkeys br-abnt2")

print("Writing brazilian mirrors to Pacman's mirrorlist.")
os.system("wget -qO- 'https://www.archlinux.org/mirrorlist/?country=BR&use_mirror_status=on' | sed 's/#S/S/g' | sed '/## Brazil/d' > /etc/pacman.d/mirrorlist")

print("Setting timezone to America/Sao_Paulo")
os.system("timedatectl set-ntp true")
os.system("timedatectl set-timezone America/Sao_Paulo")

print("Please, set your partitions now (try parted), format and mount them on /mnt. When you're done, run 'install_2.py'")
