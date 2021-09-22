#!/usr/bin/env python3

import os, subprocess

# List of packages
dvd = "libdvdread libdvdcss libdvdnav vlc"
gnome_apps = "gnome-screenshot gnome-system-monitor gnome-calculator gedit eog evince file-roller"
misc = "webp-pixbuf-loader" # WebP support

os.system(f"sudo pacman -S --noconfirm {gnome_apps} ffmpegthumbnailer xorg-xkill neofetch nemo-fileroller p7zip {dvd} {misc}")

print("Installing oh-my-zsh and its plugins")
os.system("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh) --unattended\"")
os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
os.system("sed -i -e 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/g' ~/.zshrc")

print("Installing yay")
# Build "yay" as user, since "makepkg" cannot be executed as "sudo"
os.system("cd /tmp && git clone https://aur.archlinux.org/yay-bin.git && cd /tmp/yay-bin && makepkg -s")

# Install yay
os.system(f"sudo pacman -U /tmp/yay-bin/yay-*.pkg.tar.zst --noconfirm")

os.system(f"rm -rf /tmp/yay-bin/")
