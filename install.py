#!/usr/bin/env python3

import os, re, subprocess

rows, columns = os.popen("stty size", "r").read().split()
separator = "-" * int(columns)

print("TALI (Telmo's Arch Linux Installer)")
print(separator)

text = """phy#0
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

ls_efi = subprocess.check_output("ls /sys/firmware/efi/efivars; exit 0;", shell=True, stderr=subprocess.STDOUT)
ls_efi = ls_efi.decode()

if(ls_efi[:2] == "ls"):
  boot = "BIOS"
else:
  boot = "UEFI"

print(boot)

fdisk = subprocess.check_output("fdisk -l;", shell=True, stderr=subprocess.STDOUT)
fdisk = fdisk.decode()

disks = re.findall("Disk \/\w+\/\w+", fdisk)

for x in disks:
  print(x)