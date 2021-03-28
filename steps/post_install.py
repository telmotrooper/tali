import os, subprocess
from getpass import getpass
from utils.disk_utils import select_disk
from utils.yes_no_dialog import yes_no_dialog

# List of packages
dvd = "libdvdread libdvdcss libdvdnav vlc"
gnome_apps = "gnome-screenshot gnome-system-monitor gnome-calculator gedit eog evince file-roller"
misc = "webp-pixbuf-loader" # WebP support

os.system(f"pacman -S --noconfirm {gnome_apps} ffmpegthumbnailer xorg-xkill neofetch nemo-fileroller p7zip {dvd} {misc}")

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
