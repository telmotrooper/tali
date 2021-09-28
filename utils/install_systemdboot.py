import os

from utils.get_firmware_interface import get_firmware_interface

def install_systemdboot():
    os.system("bootctl install")
    
    # TODO:
    # Check which kernels are installed
    # Find out on which drive the system was installed
    # Find out which partition is the root partition

    os.system("""echo "title   Arch Linux (Zen)
linux   /vmlinuz-linux-zen
initrd  /initramfs-linux-zen.img
options root=/dev/sda2 rw" > /boot/loader/loader.conf""")

    os.system("""echo "title   Arch Linux (Zen)
linux   /vmlinuz-linux-zen
initrd  /initramfs-linux-zen.img
options root=/dev/sda2 rw" > /boot/loader/entries/arch_zen.conf""")
