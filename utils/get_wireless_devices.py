import subprocess

def get_wireless_devices():
  iw_dev = subprocess.check_output(
    "iw dev | grep Interface | awk '{print $2}'",
    shell=True, stderr=subprocess.STDOUT).decode().rstrip().splitlines()

  if(iw_dev == ""):
    return []
  else:
    devices = []
  
    for i, device in enumerate(iw_dev):
      devices.append(iw_dev[i])
    
    return devices
