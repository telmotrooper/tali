import os

from utils.get_firmware_interface import get_firmware_interface
from utils.run_command import run_command


def install_systemdboot():
    os.system("bootctl install")
    
    kernels_installed = run_command("pacman -Q | awk '/^linux/' | awk '!/headers|firmware/' | awk '{print $1}'")

    print("Kernels installed are:")
    print(kernels_installed.splitlines())

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
