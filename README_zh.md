# PyBingWallpaper_GNOME

[English](./README.md)|[中文](./README_zh.md)

本程序用于在`GNOME`桌面环境下自动更换桌面背景为`必应每日壁纸`。

本程序会将获取到的Bing壁纸保存到`~/bingwallpaper`,同时会保留壁纸和壁纸的介绍。会将壁纸保存到`bingwallpaper%Y-%M-%D.jpg`,介绍保存到`bingwallpaper%Y-%M-%D.jpg.txt`。

## 安装

执行以下命令：

```Bash
git clone https://github.com/LRoInT/PyBingWallpaper_GNOME.git
cd PyBingWallpaper_GNOME
. install.sh
```

安装完成后可以在应用程序列表中找到，会将其添加到应用列表中。你可以设置是否自动启动（仅对当前用户有效）。

如果之前安装过，你可以选择覆盖旧文件。

## 使用

- 直接运行

```Bash
bingwallpaper
```

安装后可直接在终端输入`bingwallpaper`运行。

- 从应用列表运行
找到`必应壁纸`软件。

## 配置

配置文件保存在`~/.config/bingwallpaper.json`。可直接编辑。

## 键

1. `get`：当其为`True`是，程序会自动获取壁纸。
2. `use`：当其为`True`时，程序会自动设置当日壁纸为背景。

### 命令行

```Bash
bingwallpaper set get 1 use 1
```

1. `set`：当其在参数列表中时，程序会将配置保存到配置文件中
2. 其它：与配置文件的键对应，在其后添加`1`设置为`True`，添加`0`设置为`False`。
