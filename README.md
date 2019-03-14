# TALI (Telmo's Arch Linux Installer)

## **ATTENTION: This script is not ready for use**

## Setup

First of all, boot your [Arch Linux live CD](https://www.archlinux.org/download/).

If you're using a brazilian keyboard, you'll probably want to load the proper keyboard layout with either `loadkeys br-abnt` or `loadkeys br-abnt2`.

You'll need an internet connection to use this script, if you need to use Wi-Fi type `iw dev` to find your Wi-Fi interface name and then `wifi-menu -o INTERFACE_NAME` to connect.

Then, download the script and run it:

```
wget -q https://raw.githubusercontent.com/telmotrooper/tali/master/install.py && python install.py
```
