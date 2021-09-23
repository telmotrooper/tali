#!/usr/bin/env python3

import os, sys

print("Installing oh-my-zsh and its plugins")
os.system("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh) --unattended\"")
os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
os.system("sed -i -e 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/g' ~/.zshrc")

# Cinnamon
os.system("gsettings set org.cinnamon.desktop.wm.preferences theme 'Arc'")     # Window borders
os.system("gsettings set org.cinnamon.desktop.interface icon-theme 'Papirus'") # Icons
os.system("gsettings set org.cinnamon.desktop.interface gtk-theme 'Arc'")      # Controls
os.system("gsettings set org.cinnamon.theme name 'Arc-Dark'")                  # Desktop
# The mouse is "org.cinnamon.desktop.interface cursor-theme"
os.system("gsettings set org.gnome.libgnomekbd.keyboard layouts \"['br']\"")   # Set keyboard layout

# GNOME Terminal
os.system("dconf write /org/gnome/terminal/legacy/theme-variant \"'dark'\"")

# Remove script after it's been executed
os.remove(sys.argv[0])
