from utils.colors import cyan, green, yellow
from utils.suggest_partitioning import suggest_partitioning
from utils.yes_no_dialog import yes_no_dialog

good_to_go = yes_no_dialog("Did you set your partitions, format them and mount them on " + yellow("/mnt") + "?")

if good_to_go:
  import os

  print()
  kernel_packages = select(
    "Which kernel do you want to install?
    dict([
      ("Zen + Mainline (recommended)", "linux-zen linux-zen-headers linux linux-headers"),
      ("Zen", "linux-zen linux-zen-headers"),
      ("Mainline", "linux linux-headers")
    ])
  )

  os.system(f"pacstrap /mnt base base-devel {kernel_packages} linux-firmware net-tools xdg-user-dirs")
  os.system("pacstrap /mnt python wget")
  os.system("genfstab -U /mnt >> /mnt/etc/fstab")
  os.system("cp -r /root/tali /mnt/tali")
  os.system("cp /etc/pacman.d/mirrorlist /mnt/etc/pacman.d/mirrorlist")
  os.system("arch-chroot /mnt python tali/install.py --step 3")
else:
  suggest_partitioning()
