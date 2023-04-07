import os
from getpass import getpass

from utils.select import select
from utils.yes_no_dialog import yes_no_dialog
from utils.colors import yellow
from utils.install_systemdboot import install_systemdboot
from install import config

# Step 3 runs inside chroot environment.

# List of packages
fonts = "ttf-bitstream-vera ttf-droid noto-fonts-emoji"
themes = "arc-gtk-theme papirus-icon-theme"

config.read("/tali/tali.ini")
encrypt = bool(config["DEFAULT"]["Encrypt"])

if encrypt:
    os.system("cat /etc/mkinitcpio.conf | sed 's/ filesystems / encrypt filesystems /' > /tmp/mkinitcpio.conf")
    os.system("mv /tmp/mkinitcpio.conf /etc/mkinitcpio.conf")
    os.system("mkinitcpio -P")

install_systemdboot(encrypt)

desktop_environment = select(
    "Which desktop environment would you like to install?",
    dict([
        ("Cinnamon", "cinnamon gdm gnome-terminal"),
        ("None", "")
    ])
)

# Remaining setup
os.system(f"pacman -S --noconfirm {fonts} {desktop_environment} networkmanager firefox {themes} zsh git go")

if "gdm" in desktop_environment:
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

while (password1 != password2):
    password1 = getpass("Set your password: ")
    password2 = getpass("Repeat your password: ")

    if password1 != password2:
        print("The passwords don't match.")
print("-" * 100)

os.system(f"echo root:{password1} | chpasswd")
os.system(f"echo {username}:{password1} | chpasswd")
os.system("cat /etc/sudoers | sed 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' > /etc/sudoers_new")

enable_pwfeedback = yes_no_dialog("Would you like to enable password feedback?")

if enable_pwfeedback:
    os.system("echo '\nDefaults pwfeedback' | tee -a /etc/sudoers_new")

os.system("mv /etc/sudoers_new /etc/sudoers")

# Enable colors for Pacman (and yay)
os.system("sed -i 's/#Color/Color/g' /etc/pacman.conf")

if "gdm" in desktop_environment:  # Setup GDM to default user to Cinnamon
    os.system(f"""printf '[User]
Language=
Session=cinnamon
XSession=cinnamon
Icon=
SystemAccount=false\n\n' > /var/lib/AccountsService/users/{username}""")

# Copy last step script to user desktop and remove the remaining files
os.system(f"sudo -u {username} sh -c \"mkdir -p ~/Desktop\"")
os.system(f"sudo -u {username} sh -c \"cp /tali/steps/post_install_user.py ~/Desktop/\"")
os.system(f"sudo -u {username} sh -c \"cp /tali/steps/post_install_system.py ~/Desktop/\"")
os.system("rm -rf /tali")

print("You can restart your computer now (e.g. " + yellow("shutdown -r now") + ").")
