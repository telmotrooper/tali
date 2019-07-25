#!/usr/bin/env python3

import os, re
from func.get_firmware_interface import get_firmware_interface


print("TALI (Telmo's Arch Linux Installer)\n")

text1 = """phy#0
    Interface wlp6s0
        ifindex 3
        wdev 0x1
        addr b0:10:41:fe:bd:a7
        ssid Apartamento
        type managed
        channel 11 (2462 MHz), width: 40 MHz, center1: 2452 MHz
        txpower 16.00 dBm
        multicast TXQ:
            qsz-byt qsz-pkt flows   drops   marks   overlmt hashcoltx-bytes tx-packets
            0   0   0   0   0   0   0   00"""

text2 = ""
match_iw = re.search("Interface \w+", text2)

if(match_iw != None):
  network_interface = (match_iw.group(0).split(" ")[1])
  print("Wi-Fi interface: {}".format(network_interface))
else:
  print("No Wi-Fi interface found.")

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
