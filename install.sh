#!/usr/bin/bash

if [ ! -d ~/bin ];
then
    mkdir ~/bin
fi

# Install Python file
if [ -d ~/.local/bin/bingwallpaper ];
then
    rm ~/.local/bin/bingwallpaper
fi
sudo cp ./bingwallpaper.py ~/.local/bin/bingwallpaper
sudo chmod +x ~/.local/bin/bingwallpaper

# Set .desktop file
if [ -d ~/.local/share/applications/bingwallpaper.desktop ];
then
    rm ~/.local/share/applications/bingwallpaper.desktop
fi
sudo cp ./bingwallpaper.desktop ~/.local/share/applications/bingwallpaper.desktop

# Set autostart
if [ -d ~/.config/autostart/bingwallpaper.desktop ];
then
    rm ~/.config/autostart/bingwallpaper.desktop
fi
sudo cp ./bingwallpaper.desktop ~/.config/autostart/bingwallpaper.desktop

echo "Bing Wallpaper installed"