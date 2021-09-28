import os

from utils.get_firmware_interface import get_firmware_interface
from utils.run_command import run_command


def install_systemdboot():
    os.system("bootctl install")
    
    kernels_installed = run_command("pacman -Q | awk '/^linux/' | awk '!/atm|headers|firmware/' | awk '{print $1}'")

    print("Kernels installed are:")
    print(kernels_installed.splitlines())

    run_command(f"""echo 'default         arch_{kernels_installed[0]}.conf
timeout         1
console-mode    max
editor          no' > /boot/loader/loader.conf""")


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

    file_content = ""

    for key, value in entry.items():
        file_content += f"{key}\t{value}\n"

    run_command(f"echo '{file_content}' > /boot/loader/entries/arch_{kernel_package}.conf")
