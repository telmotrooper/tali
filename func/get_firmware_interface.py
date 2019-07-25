import subprocess

def get_firmware_interface():
  ls_efi = subprocess.check_output(
    "ls /sys/firmware/efi/efivars; exit 0;",
    shell=True,
    stderr=subprocess.STDOUT).decode()

  # The output only starts with "ls" if the command failed, which
  # is what happens when your system does not have UEFI variables.
  if(ls_efi[:2] == "ls"):
    return "BIOS"
  else:
    return "UEFI"
