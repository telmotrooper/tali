#!/usr/bin/env bash

printf "Generating mirrorlist with mirrors from Brazil for faster downloads..."
reflector --verbose --threads 4 --protocol http,https --country Brazil --age 12 --sort rate --save /etc/pacman.d/mirrorlist
cat /etc/pacman.d/mirrorlist | grep Server

printf "Downloading package \"git\"...\n"
sudo pacman -Sy git --noconfirm

printf "Cloning installer...\n"
git clone https://github.com/telmotrooper/tali.git

printf "Executing installer...\n"
tali/install.py
