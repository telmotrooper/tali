from utils.colors import cyan, green, yellow
from utils.select import select
from utils.suggest_partitioning import suggest_partitioning
from utils.yes_no_dialog import yes_no_dialog
from utils.run_command import run_command

good_to_go = yes_no_dialog("Did you set your partitions, format them and mount them on " + yellow("/mnt") + "?")

if good_to_go:
  import os

  print()
  kernel_packages = select(
    "Which kernel do you want to install?",
    dict([
      ("Zen + Mainline (recommended)", "linux-zen linux-zen-headers linux linux-headers"),
      ("Zen", "linux-zen linux-zen-headers"),
      ("Mainline", "linux linux-headers")
    ])
  )

  run_command(f"pacstrap /mnt base base-devel {kernel_packages} linux-firmware net-tools xdg-user-dirs")
  run_command("pacstrap /mnt python wget")
  run_command("genfstab -U /mnt >> /mnt/etc/fstab")
  run_command("cp -r /root/tali /mnt/tali")
  run_command("cp /etc/pacman.d/mirrorlist /mnt/etc/pacman.d/mirrorlist")
  os.system("arch-chroot /mnt python tali/install.py --step 3")
else:
  suggest_partitioning()
