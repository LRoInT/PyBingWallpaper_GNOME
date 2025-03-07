#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import requests
import os
import datetime
import json

background_dir = os.path.expanduser("~/bingwallpaper")


def get_wallpaper(nowtime, n=8) -> list:  # 获取壁纸 Get wallpaper
    if not os.path.exists(background_dir):
        # 当目录不存在时 If the dir doesn't exist
        os.mkdir(background_dir)

    wp_paths = []

    wallpaper_url = json.loads(requests.get(  # 使用API获取壁纸信息 Get wallpaper info by API
        f"https://bing.com/HPImageArchive.aspx?format=js&n={n}").text)
    d = 0
    for i in wallpaper_url["images"]:
        nt = nowtime + datetime.timedelta(days=d)
        ymd = [nt.year, nt.month, nt.day]
        if os.path.exists(wp_path := os.path.join(background_dir, f"bingwallpaper{ymd[0]}-{ymd[1]}-{ymd[2]}.jpg")):
            # 不获取重复的壁纸 Don't get repeated wallpaper
            wp_paths.append(wp_path)
        wallpaper = requests.get("https://bing.com"+i["url"])
        # 写入壁纸文件 Write wallpaper
        with open(wp_path, "wb") as f:
            f.write(wallpaper.content)
        # 写入壁纸信息 Write copyright
        with open(wp_path+".txt", "w") as f:
            f.write(f"{i['copyright']}\n{i['copyrightlink']}")
        d += 1
    return wp_paths


def set_wallpaper(wp_path: str):  # 在 GNOME 中设置壁纸 Set wallpaper in GNOME
    return os.system(
        f"gsettings set org.gnome.desktop.background picture-uri 'file://{wp_path}' && gsettings set org.gnome.desktop.background picture-uri-dark 'file://{wp_path}'")


if __name__ == '__main__':
    nowtime = datetime.datetime.now()
    wp_paths = get_wallpaper(nowtime)
    if not (r := set_wallpaper(wp_paths[0])):
        print(f"Already set wallpaper:{wp_paths[0]}")
    sys.exit(r)
