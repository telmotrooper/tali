#!/usr/bin/env python3

import os, re, subprocess

rows, columns = os.popen('stty size', 'r').read().split()
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

match = re.search("Interface (\w+)", text2)

if(match != None):
  network_interface = (match.group(0).split(" ")[1])
  print("Wi-Fi interface: {}".format(network_interface))
else:
  print("No Wi-Fi interface found.")

boot = subprocess.check_output("ls /sys/firmware/efi/efivars; exit 0;", shell=True, stderr=subprocess.STDOUT)
boot = boot.decode()

if(boot[:2] == "ls"):
  boot = "BIOS"
else:
  boot = "UEFI"

print(boot)
