#!/usr/bin/bash

install_path="$HOME/.local"

read -r -p "Install for all users? [Y/n] " response_path
if [ response_path == "y" -o response_path == "Y" ]; then
    install_path="/usr/local"
fi

# Install Python file
if [ -e $install_path/bin/bingwallpaper ]; then
    read -r -p "Remove existing Bing Wallpaper program file? [Y/n] " response_py
    if [ $response_py = "y" -o $response_py = "Y" ]; then
        rm $install_path/bin/bingwallpaper
    fi
fi
if [ ! -e $install_path/bin/bingwallpaper ]; then
    echo "Copy program"
    sudo cp ./bingwallpaper.py $install_path/bin/bingwallpaper
    echo "Add x to program"
    sudo chmod +x $install_path/bin/bingwallpaper
fi

# Set .desktop file
if [ -e $install_path/share/applications/bingwallpaper.desktop ]; then
    read -r -p "Remove existing Bing Wallpaper desktop file? [Y/n] " response_de
    if [ $response_de == "y" -o $response_de == "Y" ]; then
        rm $install_path/share/applications/bingwallpaper.desktop
    fi
fi
if [ ! -e "$install_path/share/applications/bingwallpaper.desktop" ]; then
    cp ./bingwallpaper.desktop ~/.local/share/applications/bingwallpaper.desktop
fi

echo "Installed Bing Wallpaper"

# Set autostart

read -r -p "Add bingwallpaper to auto start? [Y/n] " response_as
if [ $response_as == "y" -o $response_as == "Y" ]; then
    if [ -e ~/.config/autostart/bingwallpaper.desktop ]; then
        read -r -p "Remove existing Bing Wallpaper auto start? [Y/n] " response_as
        if [ $response_as == "y" -o $response_as == "Y" ]; then
            rm ~/.config/autostart/bingwallpaper.desktop
        fi
    fi

    if [ ! -e ~/.config/autostart/bingwallpaper.desktop ]; then
        cp ./bingwallpaper.desktop ~/.config/autostart/bingwallpaper.desktop
    fi

    echo "Added Bing Wallpaper to autostart"
fi

if [ $response_as == "n" -o $response_as == "N" ]; then
    if [ -e ~/.config/autostart/bingwallpaper.desktop ]; then
        rm ~/.config/autostart/bingwallpaper.desktop
    fi
fi
