#!/usr/bin/env python3

import os
os.system("reflector --verbose --threads 4 --protocol http,https --country Brazil --age 12 --sort rate --save /etc/pacman.d/mirrorlist")
os.system("cat /etc/pacman.d/mirrorlist | grep Server")
