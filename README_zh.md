# PyBingWallpaper_GNOME

本程序用于在`GNOME`桌面环境下自动更换`Bing`每日壁纸。

本程序会将获取到的Bing壁纸保存到`~/bingwallpaper`,同时会保留壁纸和壁纸的介绍。会将壁纸保存到`bingwallpaper%Y-%M-%D.jpg`,介绍保存到`copyright%Y-%M-%D`。

## 安装

执行以下命令：

```Bash
git clone https://github.com/LRoInT/PyBingWallpaper_GNOME.git
cd PyBingWallpaper_GNOME
bash install.sh
```

安装完成后可以在应用程序列表中找到，会设置自动启动（仅限当前用户可用）

## 使用

- 直接运行

```Bash
python3 bingwallpaper.py
```

安装后可直接在终端输入`bingwallpaper`运行

- 从应用列表运行
找到`必应壁纸`软件
