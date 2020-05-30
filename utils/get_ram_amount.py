import subprocess

def get_ram_amount():
  return subprocess.check_output(
    "free -m | grep Mem | awk '{print $2}'",
    shell=True, stderr=subprocess.STDOUT).decode().rstrip()
