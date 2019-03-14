#!/usr/bin/env python3

import os
import re

rows, columns = os.popen('stty size', 'r').read().split()
separator = "-" * int(columns)

print("Telmo's Arch Linux Installer")
print(separator)

# while True:   # do while
#   network = input("Are you using Wi-Fi or a wired network? ")

#   if(network.lower() == "wifi" or network.lower() == "wi-fi"):
#     print("Wi-Fi")
#     break
#   elif(network.lower() == "wired" or network.lower() == "ethernet"):
#     print("Wired")
#     break

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
  print("No Wi-Fi interface found")

boot = os.popen('ls /sys/firmware/efi/efivars', 'r').read()
if(boot == ''):
  boot = "BIOS"
else:
  boot = "UEFI"

print(boot)