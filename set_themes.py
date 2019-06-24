#!/usr/bin/env python3

import os

# Cinnamon
os.system("gsettings set org.cinnamon.desktop.wm.preferences theme 'Arc'")     # Window borders
os.system("gsettings set org.cinnamon.desktop.interface icon-theme 'Papirus'") # Icons
os.system("gsettings set org.cinnamon.desktop.interface gtk-theme 'Arc'")      # Controls
os.system("gsettings set org.cinnamon.theme name 'Arc-Dark'")                  # Desktop
# The mouse is "org.cinnamon.desktop.interface cursor-theme"

# GNOME Terminal
os.system("dconf write /org/gnome/terminal/legacy/theme-variant \"'dark'\"")