import os

from utils.get_firmware_interface import get_firmware_interface
from utils.yes_no_dialog import yes_no_dialog

def install_grub():
    fw_interface = get_firmware_interface()

    # Installing boot loader
    os.system(f"pacman -S --noconfirm grub os-prober")

    if (fw_interface == "UEFI"):
        os.system("pacman -S --noconfirm efibootmgr")
        os.system("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB")
    else:
        print("In which disk should GRUB be installed?")
        disk = select_disk()
        os.system(f"grub-install --target=i386-pc {disk}")

    os.system("grub-mkconfig -o /boot/grub/grub.cfg")

    should_proceed = yes_no_dialog("Proceed?")

    if not should_proceed:
        sys.exit()
