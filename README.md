# TALI (Telmo's Arch Linux Installer)

![](tali.png)

## Setup

First of all, boot your [Arch Linux live CD](https://www.archlinux.org/download/).

You'll need an active internet connection to use the script, if you need to use Wi-Fi type `iwctl` to find your Wi-Fi network and connect to it.

You'll also probably want to load the brazilian keyboard layout:
```
loadkeys br-abnt2
```

Then, proceed to download the script and run it:

```
curl -L https://git.io/tali | bash
```

## Additional info

If for some reason you'd like to clone a specific branch and run that version of the script, you can instead use:
```
curl -L https://git.io/tali | bash -s BRANCH_NAME
```

If you'd like to see contents of the script you're about to execute, you can use:
```
curl -L https://git.io/tali | less
```
