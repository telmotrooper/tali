import os

from utils.get_firmware_interface import get_firmware_interface
from utils.run_command import run_command


def install_systemdboot():
    os.system("bootctl install")
    
    kernels_installed = run_command("pacman -Q | awk '/^linux/' | awk '!/atm|headers|firmware/' | awk '{print $1}'")
    
    generate_loader_config(kernels_installed[0])
    
    # TODO:
    # [x] Check which kernels are installed
    # Find out on which drive the system was installed
    # Find out which partition is the root partition

    temp_partition = "/dev/sda2"

    for kernel in kernels_installed.splitlines():
        generate_entry(kernel, temp_partition)

def generate_entry(kernel_package: str, root_partition: str):
    print(f'Generating boot entry for "{kernel_package}"...')
    entry = dict()
    entry["title"] = f"Arch Linux ({kernel_package})"
    entry["linux"] = f"/vmlinuz-{kernel_package}"
    entry["initrd"] = f"/initramfs-{kernel_package}.img"
    entry["options"] = f"root={root_partition} rw"

    file_content = dict_to_file_content(entry)
    run_command(f"echo '{file_content}' > /boot/loader/entries/arch_{kernel_package}.conf")

def generate_loader_config(default_kernel: str):
    config = dict()
    config["default"] = f"arch_{default_kernel}.conf"
    config["timeout"] = 1
    config["console-mode"] = "max"
    config["editor"] = "no"

    file_content = dict_to_file_content(config)
    run_command(f"echo '{file_content}' > /boot/loader/loader.conf")

def dict_to_file_content(entries: dict):
    file_content = ""

    for key, value in entries.items():
        file_content += f"{key}\t{value}\n"
    
    return file_content
