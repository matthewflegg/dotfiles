# dotfiles
Personal dotfiles for my Arch build on my main PC. This is what it looks like:

![Qtile Screenshot](https://user-images.githubusercontent.com/88111643/172254237-cd5f099f-bb65-4687-898e-5e54c606ec82.png)

## Prerequisites
This assumes you already have a minimal install of Arch with Xorg, Qtile, and Nvidia's proprietary driver, and have set up users, installed a bootloader, etc.

Install paru, an AUR (Arch User Repository) helper and `pacman` wrapper.

```bash
sudo pacman -S git  # Only necessary if you do not already have Git.
git clone https://aur.archlinux.org/paru-bin
cd paru-bin
makepkg
```

## Required Packages
First, some packages need to be installed. Use the commands below using `paru`.

```bash
paru -S pamixer \                 # CLI volume mixer, we will attach keybindings for it
        ttf-ubuntu-font-family \  # These fonts 
        alacritty                 # Terminal emulator
```
*Note: If you don't have volume buttons on your keyboard, you can skip `pamixer`.*

We also need pip, to install a python dependency for the net widget in Qtile:

```bash
paru -S python-pip
sudo -H pip install psutil
```

That's it. I like running a minimal build, so this is all we will be installing. There are options for GUI packages if you don't like this, however:

```bash
paru -S thunar \   # File manager
        blueman \  # Bluetooth manager
        dmenu      # Application launcher
```

## Loading my config
This is relatively simple. Just clone the repository and reload Qtile.

```bash
git clone https://github.com/matthewflegg/dotfiles
cd dotfiles
mkdir ~/.config  # Only necessary if you don't have this. Run ls ~ to see if you do.
cp -r config/qtile/ ~/.config/qtile/
cp -r config/alacritty/ ~/.config/alacritty/
```

You should now have my config loaded and working.
