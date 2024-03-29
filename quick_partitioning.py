#!/usr/bin/env python3

import os
import argparse
from utils.get_ram_amount import get_ram_amount
from utils.disk_utils import select_disk
from utils.get_firmware_interface import get_firmware_interface
from utils.colors import cyan, green, yellow
from utils.yes_no_dialog import yes_no_dialog
from install import config, path, write_config_file


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--format-and-mount", default=True)
    args = parser.parse_args()

    if isinstance(args.format_and_mount, str):  # Parse string to boolean.
        match args.format_and_mount.lower():
            case "true":
                args.format_and_mount = True
            case "false":
                args.format_and_mount = False

    ram = get_ram_amount()

    print("Which disk should be partitioned? ")
    disk = select_disk()

    encrypt = yes_no_dialog("Would you like to encrypt your system using dm-crypt and LUKS?")

    suffix = "p" if ("nvme" in disk) else ""  # NVMe numbers partitions as p1, p2, p3 instead of 1, 2, 3.

    use_swap = False if encrypt else yes_no_dialog(
        f"We detected {ram} MiB of RAM, should we create a swap partition of the same size?")

    fw_interface = get_firmware_interface()

    # Boot partition size (MiB)
    boot_bios = 261
    boot_uefi = 261
    boot_size = boot_uefi if fw_interface == "UEFI" else boot_bios

    swap_end = int(ram) + boot_size

    parted_command = ""

    if fw_interface == "BIOS":
        if use_swap:
            parted_command = f"""
        parted --script {disk} \
        mklabel msdos \
        mkpart primary ext4 1MiB {boot_size}MiB \
        set 1 boot on \
        mkpart primary linux-swap {boot_size}MiB {swap_end}MiB \
        mkpart primary ext4 {swap_end}MiB 100%"""
        else:
            parted_command = f"""
        parted --script {disk} \
        mklabel msdos \
        mkpart primary ext4 1MiB {boot_size}MiB \
        set 1 boot on \
        mkpart primary ext4 {boot_size}MiB 100%"""

    else:  # UEFI
        if use_swap:
            parted_command = f"""
        parted --script {disk} \
        mklabel gpt \
        mkpart primary fat32 1MiB {boot_size}MiB \
        set 1 esp on \
        mkpart primary linux-swap {boot_size}MiB {swap_end}MiB \
        mkpart primary ext4 {swap_end}MiB 100%"""
        else:
            parted_command = f"""
        parted --script {disk} \
        mklabel gpt \
        mkpart primary fat32 1MiB {boot_size}MiB \
        set 1 esp on \
        mkpart primary ext4 {boot_size}MiB 100%"""

    if args.debug:
        print(parted_command)

    os.system(parted_command)

    if args.format_and_mount:
        print("--- Formatting partitions ---")

        partition_number = 1

        if fw_interface == "BIOS":
            os.system(f"mkfs.ext4 {disk}{suffix}{partition_number}")
        else:  # UEFI
            os.system(f"mkfs.fat -F32 {disk}{suffix}{partition_number}")

        partition_number += 1

        if use_swap:
            os.system(f"mkswap {disk}{suffix}")
            os.system(f"swapon {disk}{suffix}{partition_number}")
            partition_number += 1

        if encrypt:
            os.system(f"cryptsetup -y -v luksFormat {disk}{suffix}{partition_number}")
            print("\nYou will have to enter your password again to unlock the partition.\n")
            os.system(f"cryptsetup open {disk}{suffix}{partition_number} cryptroot")
            os.system("mkfs.ext4 /dev/mapper/cryptroot")

            config.read(path)
            config.set("DEFAULT", "Encrypt", str(True))
            write_config_file()
        else:
            os.system(f"mkfs.ext4 {disk}{suffix}{partition_number}")

        print("--- Mounting partitions ---")
        if encrypt:
            os.system("mount /dev/mapper/cryptroot /mnt")
        else:
            os.system(f"mount {disk}{suffix}{partition_number} /mnt")

        # These steps are the same for all combinations
        os.system(f"mkdir /mnt/boot")
        os.system(f"mount {disk}{suffix}1 /mnt/boot")

    print("You're all set, run " + green("tali/install.py") + " to continue installing " + cyan("Arch Linux") + ".")


if __name__ == "__main__":
    main()
