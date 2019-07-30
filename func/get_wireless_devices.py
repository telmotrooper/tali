import subprocess

def get_wireless_devices():
  wl_devices = subprocess.check_output(
    "iw dev | grep Interface | awk '{print $2}'",
    shell=True, stderr=subprocess.STDOUT).decode().rstrip()

  if(wl_devices == ""):
    return []
  else:
    temp = []
  
    for i, device in enumerate(wl_devices):
      temp.push(wl_devices)
    
    return temp


print(get_wireless_devices())
