import subprocess

def get_firmware_interface():
  # We use "exit 0" so we can read the output even if the command fails.
  ls_efi_vars = subprocess.check_output(
    "ls /sys/firmware/efi/efivars; exit 0;",
    shell=True,
    stderr=subprocess.STDOUT).decode()

  # The output only starts with "ls" if the command failed, which
  # is what happens when your system does not have UEFI variables.
  if(ls_efi_vars[:2] == "ls"):
    return "BIOS"
  else:
    return "UEFI"
