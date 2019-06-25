#!/usr/bin/env python3

import os, subprocess

os.system("pacman -S --noconfirm ttf-bitstream-vera grub "
  "gdm cinnamon gnome-terminal firefox gnome-system-monitor "
  "arc-gtk-theme papirus-icon-theme zsh git go ttf-droid xorg-xkill neofetch")

os.system("systemctl enable gdm")
os.system("systemctl enable NetworkManager")

os.system("ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime")
os.system("hwclock --systohc")
os.system("cat /etc/locale.gen | sed 's/#en_US.UTF-8/en_US.UTF-8/g' > /locale.gen")
os.system("mv /locale.gen /etc/")
os.system("locale-gen")
os.system("echo 'LANG=en_US.UTF-8' > /etc/locale.conf")
os.system("echo 'KEYMAP=br-abnt2' > /etc/vconsole.conf")

hostname = input("Set your computer's name: ")
os.system("echo '{}' > /etc/hostname".format(hostname))

print("Set the root password")
os.system("passwd")
username = input("Set your username: ")
os.system("useradd -m -G wheel -s /bin/zsh {}".format(username))
print("Set the password for {}".format(username))
os.system("passwd {}".format(username))
os.system("cat /etc/sudoers | sed 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' > /etc/sudoers_new")
os.system("mv /etc/sudoers_new /etc/sudoers")

# Install "oh-my-zsh"
os.system("sudo -u {} sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh) --unattended\"".format(username))

# Install "zsh-autosuggestions"
os.system("sudo -u {} sh -c \"git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions\"".format(username))

# Install "zsh-syntax-highlighting"
os.system("sudo -u {} sh -c \"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting\"".format(username))

# Build "yay" as user, since "makepkg" cannot be executed as "sudo"
os.system("sudo -u {} sh -c \"cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -s\"".format(username))

# Install yay
os.system("pacman -U /home/{}/yay/yay-*.pkg.tar.xz --noconfirm".format(username))

os.system("rm -rf /home/{}/yay/".format(username))

ls_efi = subprocess.check_output(
  "ls /sys/firmware/efi/efivars; exit 0;",
  shell=True, stderr=subprocess.STDOUT).decode()

if(ls_efi[:2] == "ls"):
  boot = "BIOS"
else:
  boot = "UEFI"

if(boot == "UEFI"):
  os.system("pacman -S --noconfirm efibootmgr")
  os.system("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB")
else:
  print("The disks available are: ")
  os.system("fdisk -l | grep 'Disk /' | awk '{print $2, $3, $4}'")
  disk = input("In which disk should GRUB be installed? ")
  os.system("grub-install --target=i386-pc {}".format(disk))

os.system("grub-mkconfig -o /boot/grub/grub.cfg")

os.system("rm install_3.py")