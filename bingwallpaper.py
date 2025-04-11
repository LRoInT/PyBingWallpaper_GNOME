#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import requests
import os
import datetime
import json


WALLPAPER_PATH = os.path.expanduser("~/bingwallpaper")
CONFIG_PATH = os.path.expanduser("~/.config/bingwallpaper.json")

if not os.path.exists(config_path := os.path.expanduser(CONFIG_PATH)):
    # 创建配置文件 Create config file
    with open(config_path, "w") as f:
        json.dump({"get": True,
                   "use": True},
                  f)
config = json.load(open(os.path.expanduser(CONFIG_PATH)))


def set_config_cli(argv: list):
    for i in argv:
        if i in config:
            key = i
        elif i.isdigit():
            config[key] = True if int(i) else False
        else:
            print(f"Error: Invalid argument {i}")


def get_wallpaper(nowtime=None, n=8) -> list:  # 获取壁纸 Get wallpaper
    if nowtime is None:
        nowtime = datetime.datetime.now()
    if not os.path.exists(WALLPAPER_PATH):
        # 当目录不存在时 If the dir doesn't exist
        os.mkdir(WALLPAPER_PATH)

    wp_paths = []

    wallpaper_url = json.loads(requests.get(  # 使用API获取壁纸信息 Get wallpaper info by API
        f"https://bing.com/HPImageArchive.aspx?format=js&n={n}").text)
    d = 0
    for i in wallpaper_url["images"]:
        nt = nowtime + datetime.timedelta(days=-d)
        ymd = [nt.year, nt.month, nt.day]
        wp_paths.append(os.path.join(
            WALLPAPER_PATH, f"bingwallpaper{ymd[0]}-{ymd[1]}-{ymd[2]}.jpg"))
        if os.path.exists(wp_paths[-1]):
            # 不获取重复的壁纸 Don't get repeated wallpaper
            pass
        else:
            wallpaper = requests.get("https://bing.com"+i["url"])
            # 写入壁纸文件 Write wallpaper
            with open(wp_paths[-1], "wb") as f:
                f.write(wallpaper.content)
            # 写入壁纸信息 Write copyright
            with open(wp_paths[-1]+".txt", "w") as f:
                f.write(f"{i['copyright']}\n{i['copyrightlink']}")
        d += 1
    return wp_paths


def set_wallpaper(wp_path: str):  # 在 GNOME 中设置壁纸 Set wallpaper in GNOME
    wp_path = os.path.join(WALLPAPER_PATH, wp_path)
    return os.system(
        f"gsettings set org.gnome.desktop.background picture-uri 'file:{wp_path}' && gsettings set org.gnome.desktop.background picture-uri-dark 'file://{wp_path}' && echo 'file://{wp_path}' >> ~/bingwallpaper/log")


if __name__ == '__main__':
    r = 0
    if len(sys.argv) > 1:
        if sys.argv[1] == "set":
            set_config_cli(sys.argv[2:])
            with open(os.path.expanduser(CONFIG_PATH), "w") as f:
                json.dump(config, f)
        else:
            set_config_cli(sys.argv[1:])
    if config["get"]:
        wp_paths = get_wallpaper()
    else:
        wp_paths = sorted([i for i in os.listdir(  # 从本地加载壁纸，并选择最新的 Load wallpaper from local, and choose the last one
            WALLPAPER_PATH) if i.endswith(".jpg")], reverse=True, key=lambda file: [int(i) for i in file[14:-4].split("-")])
    if config["use"]:
        if not wp_paths:
            print("Error: No wallpaper to set")
            sys.exit(1)
        if r := set_wallpaper(wp_paths[0]):
            print(f"Error: {r}")
        else:
            print(f"Success set {wp_paths[0]}")
    sys.exit(r)
