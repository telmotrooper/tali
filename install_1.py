#!/usr/bin/env python3

import os, re
from func.get_firmware_interface import get_firmware_interface
from func.get_wireless_devices import get_wireless_devices
from func.disk_utils import get_disks
from func.print_logo import print_logo
from func.colors import cyan, green, yellow

print_logo()

wl_devices = get_wireless_devices()

if(wl_devices != []): # at least one wireless device was found
  print("The following Wi-Fi devices were found:")
  for device in wl_devices:
    print(device)
else:
  print("No Wi-Fi device found")

print("\nYou're running " + yellow(f"{get_firmware_interface()}"))

disks = get_disks()

print("\nThe following disks were found:")

for disk in disks:
  print(disk)

print("\nSetting keyboard layout to " + yellow("br-abnt2"))
os.system("loadkeys br-abnt2")

print("Writing brazilian mirrors to Pacman's mirrorlist")
os.system("wget -qO- 'https://www.archlinux.org/mirrorlist/?country=BR&use_mirror_status=on' | sed 's/#S/S/g' | sed '/## Brazil/d' > /etc/pacman.d/mirrorlist")

print("Setting timezone to " + yellow("America/Sao_Paulo"))
os.system("timedatectl set-ntp true")
os.system("timedatectl set-timezone America/Sao_Paulo")

print("\nPlease, set your partitions now, format and mount them on " + yellow("/mnt") + ".")
print("If all you want to do is to wipe all partitions and install " + cyan("Arch Linux") + ", you can run " + green("quick_partitioning.py") + ".")
print("Otherwise, you can format your partitions yourself with " + green("parted") + " or a similar tool.")
print("\nWhen you're done, run " + green("install_2.py") + ".\n")
