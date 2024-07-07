#!/usr/bin/env bash
# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
# 
#

# Install bin scripts
function bin_scripts(){
    mkdir -p ~/.local/bin
    cp -ru ~/dots/bin/* ~/.local/bin
    if [ "$(ls -A ~/.local/bin)" ]; then
        chmod +x ~/.local/bin/*
    fi
}

# Copy Qtile Files
function qtile_files(){
    mkdir -p ~/.config/qtile
    cp -r ~/dots/qtile/* ~/.config/qtile/
}

# Copy Dotfiles
function copy_dotfiles(){
    cp .shortcuts ~/
}

# Install Lightdm
function install_lightdm(){
    sudo cp ~/dots/lightdm/lightdm.conf /etc/lightdm/
    sudo cp ~/dots/lightdm/lightdm-webkit2-greeter.conf /etc/lightdm/
    sudo cp ~/dots/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/
    sudo cp -r ~/dots/lightdm/theme/SpectrumOS /usr/share/lightdm-webkit/themes/
    sudo cp ~/.cache/wal/colors.css /usr/share/lightdm-webkit/themes/SpectrumOS/css/
}


#bin_scripts
#qtile_files
#copy_dotfiles
install_lightdm