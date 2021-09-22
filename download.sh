#!/usr/bin/env bash

printf "Downloading package \"git\"...\n"
sudo pacman -Sy git --noconfirm

printf "Cloning installer...\n"
git clone https://github.com/telmotrooper/tali.git

printf "Executing installer...\n"
tali/install.py

