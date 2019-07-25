import subprocess

def get_firmware_interface():
  ls_efi = subprocess.check_output(
    "ls /sys/firmware/efi/efivars; exit 0;",
    shell=True,
    stderr=subprocess.STDOUT).decode()

  if(ls_efi[:2] == "ls"):
    return "BIOS"
  else:
    return "UEFI"
