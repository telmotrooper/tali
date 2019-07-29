#!/usr/bin/env python3

import os, subprocess
from getpass import getpass
from func.select_disk import select_disk

os.system("pacman -S --noconfirm ttf-bitstream-vera grub "
  "gdm cinnamon gnome-terminal firefox gnome-system-monitor "
  "arc-gtk-theme papirus-icon-theme zsh git go ttf-droid xorg-xkill neofetch")

print("Enabling the display manager")
os.system("systemctl enable gdm")
os.system("systemctl enable NetworkManager")

print("Synchroning the clock")
os.system("ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime")
os.system("hwclock --systohc")

print("Setting up locale")
os.system("cat /etc/locale.gen | sed 's/#en_US.UTF-8/en_US.UTF-8/g' > /locale.gen")
os.system("mv /locale.gen /etc/")
os.system("locale-gen")
os.system("echo 'LANG=en_US.UTF-8' > /etc/locale.conf")
os.system("echo 'KEYMAP=br-abnt2' > /etc/vconsole.conf")

hostname = input("Set your computer's name: ")
os.system("echo '{}' > /etc/hostname".format(hostname))

username = input("Set your username: ")
os.system("useradd -m -G wheel -s /bin/zsh {}".format(username))

password1 = "1"
password2 = "2"

while(password1 != password2):
  password1 = getpass("Set your password: ")
  password2 = getpass("Repeat your password: ")
  
  if password1 != password2:
    print("The passwords don't match.")

os.system(f"echo root:{password1} | chpasswd")
os.system(f"echo {username}:{password1} | chpasswd")
os.system("cat /etc/sudoers | sed 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' > /etc/sudoers_new")
os.system("mv /etc/sudoers_new /etc/sudoers")

print("Installing oh-my-zsh and its plugins")
os.system("sudo -u {} sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh) --unattended\"".format(username))
os.system("sudo -u {} sh -c \"git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions\"".format(username))
os.system("sudo -u {} sh -c \"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting\"".format(username))

print("Installing yay")
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
  print("Which disk should be partitioned? ")
  print("In which disk should GRUB be installed?")
  disk = select_disk()
  os.system("grub-install --target=i386-pc {}".format(disk))

os.system("grub-mkconfig -o /boot/grub/grub.cfg")
