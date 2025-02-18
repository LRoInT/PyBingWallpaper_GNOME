#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import requests
from ast import literal_eval
import os
import datetime

background_dir = os.path.expanduser("~/bingwallpaper")

def get_wallpaper():  # get wallpaper
    nt = datetime.datetime.now()
    ymd=[nt.year, nt.month, nt.day]
    if not os.path.exists(background_dir):
        # If the directory does not exist
        os.mkdir(background_dir)
    elif os.path.exists(wp_path:=os.path.join(background_dir,f"bingwallpaper{ymd[0]}-{ymd[1]}-{ymd[2]}.jpg")):
        # If today's wallpaper has been downloaded
        return wp_path
    elif os.path.exists(wp_path:=os.path.join(background_dir,f"bingwallpaper{ymd[0]}-{ymd[1]}-{ymd[2]}.jpg")):
        # If today's wallpaper has been downloaded
        return wp_path
    wallpaper_url = literal_eval(requests.get(
        'https://bing.biturl.top/').text)
    wallpaper = requests.get(wallpaper_url['url']).content
    if not os.path.exists(background_dir):
        os.mkdir(background_dir)
    with open(wp_path := os.path.join(background_dir, f"bingwallpaper{ymd[0]}-{ymd[1]}-{ymd[2]}.jpg"), "wb") as f: # write wallpaper
        f.write(wallpaper)
    with open(os.path.join(background_dir, f"copyright{ymd[0]}-{ymd[1]}-{ymd[2]}"), "w") as f: # write copyright
        f.write(wallpaper_url["copyright"])
    return wp_path


def set_wallpaper(wp_path):  # set wallpaper
    print(wp_path,f"gsettings set org.gnome.desktop.background picture-uri 'file://{wp_path}' && gsettings set org.gnome.desktop.background picture-uri-dark 'file://{wp_path}'")
    os.system(
        f"gsettings set org.gnome.desktop.background picture-uri 'file://{wp_path}' && gsettings set org.gnome.desktop.background picture-uri-dark 'file://{wp_path}'")


if __name__ == '__main__':
    wp_path = get_wallpaper()
    set_wallpaper(wp_path)
    sys.exit(0)