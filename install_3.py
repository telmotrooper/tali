#!/usr/bin/env python3

import os

os.system("ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime")
os.system("hwclock --systohc")
