import os, re
from utils.get_firmware_interface import get_firmware_interface
from utils.get_wireless_devices import get_wireless_devices
from utils.disk_utils import get_disks
from utils.print_logo import print_logo
from utils.colors import cyan, green, yellow

country = "Brazil"
keyboard = "br-abnt2"
timezone = "America/Sao_Paulo"

print_logo()

wireless_devices = get_wireless_devices()

if(wireless_devices != []): # at least one wireless device was found
  print("The following Wi-Fi devices were found:")
  for device in wireless_devices:
    print(device)
else:
  print("No Wi-Fi device found")

print("\nYou're running " + yellow(f"{get_firmware_interface()}"))

disks = get_disks()

print("\nThe following disks were found:")

for disk in disks:
  print(disk)

print("\nSetting keyboard layout to " + yellow(keyboard))
os.system(f"loadkeys {keyboard}")

print(f"Writing mirrors from {country} to the Pacman mirrorlist")
os.system(f"reflector --verbose --threads 4 --protocol http,https --country {country} --age 12 --sort rate --save /etc/pacman.d/mirrorlist")

print("Setting timezone to " + yellow(timezone))
os.system("timedatectl set-ntp true")
os.system(f"timedatectl set-timezone {timezone}")

print("\nPlease, set your partitions now, format and mount them on " + yellow("/mnt") + ".")
print("If all you want to do is to wipe all partitions and install " + cyan("Arch Linux") + ", you can run " + green("tali/quick_partitioning.py") + ".")
print("Otherwise, you can format your partitions yourself with " + green("parted") + " or a similar tool.")
print("\nWhen you're done, run " + green("tali/install.py") + " again.\n")
