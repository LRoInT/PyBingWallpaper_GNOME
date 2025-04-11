# PyBingWallpaper_GNOME

[English](./README.md)|[中文](./README_zh.md)

This program automatically changes your GNOME desktop wallpaper to the Bing daily image.

The program saves the downloaded Bing wallpaper and its copyright information to the `~/bingwallpaper` directory. The wallpaper is saved as `bingwallpaper%Y-%M-%D.jpg`, and the copyright information is saved as `bingwallpaper%Y-%M-%D.jpg.txt`.

## Installation

Execute the following commands:

```Bash
git clone https://github.com/LRoInT/PyBingWallpaper_GNOME.git
cd PyBingWallpaper_GNOME
. install.sh
```

It will install to `~/.local/bin/bingwallpaper` and add it to program list, you can choose to add it to auto start.

If you installed it before, you can choose to overwrite the old files.

## Usage

Run directly:

```Bash
bingwallpaper
```

After installation, you can run the program by simply typing bingwallpaper in your terminal.

Run from the application list:
Find the "Bing Wallpaper" application in your application list and run it.

## Config

The config file is at `~/.config/bingwallpaper.json`. You can edit it to change the settings.

### Key

1. `get`: When it is `True`, the program will download the wallpaper.
2. `use`: When it is `True`, the program will set today's wallpaper as background.

### By CLI

```Bash
bingwallpaper set get 1 use 1
```

1. `set`: If is is in argv, the program will save the config to the config file.
2. Others: Same as the keys of config, add `1` after the key to set it to `True`, and add `0` to set it to `False`.
