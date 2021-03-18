import os, subprocess
from getpass import getpass
from utils.disk_utils import select_disk
from utils.yes_no_dialog import yes_no_dialog

# List of packages
dvd = "libdvdread libdvdcss libdvdnav vlc"
fonts = "ttf-bitstream-vera ttf-droid noto-fonts-emoji"
gnome_apps = "gnome-terminal gnome-screenshot gnome-system-monitor gedit eog evince file-roller"
misc = "webp-pixbuf-loader" # WebP support
themes = "arc-gtk-theme papirus-icon-theme"

os.system("pacman -S --noconfirm  grub os-prober " + fonts + " " + gnome_apps + " " +
  "gdm cinnamon firefox ffmpegthumbnailer " + themes + " " +
  "zsh git go xorg-xkill "
  "neofetch nemo-fileroller p7zip os-prober " + dvd + " " + misc)

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

print("-" * 100)
hostname = input("Set your computer's name: ")
os.system(f"echo '{hostname}' > /etc/hostname")

username = input("Set your username: ")
os.system(f"useradd -m -G wheel -s /bin/zsh {username}")

password1 = "1"
password2 = "2"

while(password1 != password2):
  password1 = getpass("Set your password: ")
  password2 = getpass("Repeat your password: ")
  
  if password1 != password2:
    print("The passwords don't match.")
print("-" * 100)

os.system(f"echo root:{password1} | chpasswd")
os.system(f"echo {username}:{password1} | chpasswd")
os.system("cat /etc/sudoers | sed 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' > /etc/sudoers_new")
os.system("mv /etc/sudoers_new /etc/sudoers")

# Enable colors for Pacman (and yay)
os.system("sed -i 's/#Color/Color/g' /etc/pacman.conf")

print("Installing oh-my-zsh and its plugins")
os.system(f"sudo -u {username} sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh) --unattended\"")
os.system(f"sudo -u {username} sh -c \"git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions\"")
os.system(f"sudo -u {username} sh -c \"git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting\"")
os.system(f"sudo -u {username} sh -c \"sed -i -e 's/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/g' ~/.zshrc\"")

print("Installing yay")
# Build "yay" as user, since "makepkg" cannot be executed as "sudo"
os.system(f"sudo -u {username} sh -c \"cd ~ && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -s\"")

# Install yay
os.system(f"pacman -U /home/{username}/yay-bin/yay-*.pkg.tar.zst --noconfirm")

os.system(f"rm -rf /home/{username}/yay-bin/")

# Setup GDM to default user to Cinnamon
os.system(f"""printf '[User]
Language=
Session=
XSession=cinnamon
Icon=
SystemAccount=false\n\n' > /var/lib/AccountsService/users/{username}""")

# Copy last step script to user desktop and remove the remaining files
os.system(f"sudo -u {username} sh -c \"mkdir -p ~/Desktop\"")
os.system(f"sudo -u {username} sh -c \"cp /tali/set_themes_and_kb_layout.py ~/Desktop/\"")
os.system("rm -rf /tali")

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
  print("In which disk should GRUB be installed?")
  disk = select_disk()
  os.system(f"grub-install --target=i386-pc {disk}")

os.system("grub-mkconfig -o /boot/grub/grub.cfg")
