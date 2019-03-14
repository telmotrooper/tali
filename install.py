#!/usr/bin/env python3

import os

rows, columns = os.popen('stty size', 'r').read().split()
separator = "-" * int(columns)

print("Telmo's Arch Linux Installer")
print(separator)
