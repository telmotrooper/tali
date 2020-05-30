import subprocess

def select_disk():
  disks_found = get_disks()

  for i, disk in enumerate(disks_found):
    print(f"{i+1}. {disk}")
  
  user_input = 0

  while(user_input < 1 or user_input > len(disks_found)):
    try:
      user_input = int(input("Select a disk: "))

      if(user_input < 1 or user_input > len(disks_found)):
        raise ValueError
    
    except ValueError:
      print("Invalid input")
      continue

  return disks_found[user_input-1].split()[0]

def get_disks():
  disks_found = subprocess.check_output(
    "fdisk -l | grep 'Disk /' | awk '{print $2, $3, $4}'",
    shell=True, stderr=subprocess.STDOUT).decode()
  
  disks_found = disks_found.replace(': ', ' (').replace(',', ')')
  return disks_found.splitlines()
