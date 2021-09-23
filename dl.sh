#!/usr/bin/env bash

branch_name=main

if [ -z "$1" ]
  then
    echo "Default branch"
  else
    branch_name=$1
fi

printf "Generating mirrorlist with mirrors from Brazil for faster downloads...\n"
reflector --verbose --threads 4 --protocol http,https --country Brazil --age 12 --sort rate --save /etc/pacman.d/mirrorlist
cat /etc/pacman.d/mirrorlist | grep Server

printf "Downloading package \"git\"...\n"
sudo pacman -Sy git --noconfirm

printf "Cloning installer from branch $branch_name...\n"
git clone --branch $branch_name https://github.com/telmotrooper/tali.git

printf "Executing installer...\n"
tali/install.py
