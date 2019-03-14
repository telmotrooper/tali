#!/usr/bin/env python3

import os

rows, columns = os.popen('stty size', 'r').read().split()
separator = "-" * int(columns)

print("Telmo's Arch Linux Installer")
print(separator)

while True:   # do while
  network = input("Are you using Wi-Fi or a wired network? ")

  if(network.lower() == "wifi" or network.lower() == "wi-fi"):
    print("Wi-Fi")
    break
  elif(network.lower() == "wired" or network.lower() == "ethernet"):
    print("Wired")
    break

