#!/usr/bin/env python3

import os
os.system("reflector --verbose --country Brazil --age 12 --sort rate --save /etc/pacman.d/mirrorlist")
os.system("cat /etc/pacman.d/mirrorlist | grep Server")
