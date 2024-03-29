import os, sys
from utils.colors import green, yellow
from utils.get_firmware_interface import get_firmware_interface
from utils.get_wireless_devices import get_wireless_devices
from utils.disk_utils import get_disks
from utils.print_logo import print_logo
from utils.suggest_partitioning import suggest_partitioning

country = "Brazil"
keyboard = "br-abnt2"
timezone = "America/Sao_Paulo"

print_logo()

wireless_devices = get_wireless_devices()

if wireless_devices:  # at least one wireless device was found
    print("The following Wi-Fi devices were found:")
    for device in wireless_devices:
        print(device)
else:
    print("No Wi-Fi device found")


fw_interface = get_firmware_interface()

print("\nYou're running in " + yellow(fw_interface) + " mode")

if fw_interface == "BIOS":
    print(f"\nThis script does not support BIOS, please boot in {green('UEFI')} mode if possible.\n")
    sys.exit()

disks = get_disks()

print("\nThe following disks were found:")

for disk in disks:
    print(disk)

print("\nSetting keyboard layout to " + yellow(keyboard))
os.system(f"loadkeys {keyboard}")

print("Setting timezone to " + yellow(timezone))
os.system("timedatectl set-ntp true")
os.system(f"timedatectl set-timezone {timezone}")

suggest_partitioning()
