---
title: 使用 yt-dlp 定时下载 youtube 频道视频并且上传到 onedrive
number: 23
slug: discussions-23/
url: https://github.com/tarenaexit/mkdocs-merterial-garden/discussions/23
date: 2024-06-11
authors: [tarenaexit]
categories: 
  - 1.3-运维
labels: ['1.3.2-工具']
---

> 来源：[使用 yt-dlp 定时下载 youtube 频道视频并且上传到 onedrive](https://www.yetpage.com/archives/229)
> [rclone安装](https://rclone.org/install/) 包括unzip安装
> [man-db安装](https://linux.cn/article-16270-1.html)

### 1 yt-dlp介绍

yt-dlp 是非常牛的项目，可以用来下载国内外绝大部分网站的视频。它是基于现已停用的 youtube-dlc 的 youtube-dl 分支。yt-dlp 这个项目的主要重点是添加新功能和补丁，同时会与原始项目保持同步。

### 2 linux上安装

#### 2.1 安装发行版，注意平台差异

``` bash
# amd 
wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux
# arm64
wget -O yt-dlp_linux https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux_aarch64

mv yt-dlp_linux /usr/bin/yt-dlp
chmod +x /usr/bin/yt-dlp
```

#### 2.2 debian/ubuntu安装ffmpeg，用于视频转码:

```bash
apt-get update -y
apt-get install ffmpeg man-db unzip -y
ffmpeg -version
```

#### 2.3 使用过程中报错解决

* 报错提示"ERROR: 'latin-1' codec can't encode characters in position 36-37: ordinal not in range\(256\)":
* 这个错误提示，表示某些字符无法被编码为 latin-1 字符集。通常情况下，这是由于操作系统或 shell 配置不正确所致。
* 设置环境变量 LANG 为一个合适的区域设置 \(locale\)，如 en\_US.UTF-8 或者 C.UTF-8
  ```bash
  echo "export LANG=C.UTF-8" >> ~/.bashrc
  reboot
  ```

### 3 简单命令指南

#### 3.1 参数介绍

**\-f ba+bv \-P /path/to/save\_directory**

* \-f ba+bv，最好的画质与音频
* \-P /path/to/save\_directory，下载文件的保存目录

**\--cookies /path/to/cookies**

* 加载账号cookies文件；
* youtube"成人视频"/非公开视频需要账号cookies才能下载;
* chrome浏览器可用EditThisCookie插件获取cookies，导出格式为"Netscape http cookie file"

**\--download-archive videos.txt**

* 下载前，yt-dlp 查看videos.txt文件，不下载该文件中记录的视频；
* 下载后，yt-dlp 将已完成下载的视频id，记录到videos.txt文件中;
* 此参数可避免视频重复下载，常用来追更。

**\-o '\%\(channel\_id\)s/\%\(playlist\_id\)s/\%\(id\)s.\%\(ext\)s'**

* 自定义文件的"保存位置与重命名"；
* 此处为"./频道id/播放列表id/视频id.视频后缀\[如mp4\]"

#### 3.2 下载示范

```
以最好的画质与音频下载视频，不加载cookies
yt-dlp -f ba+bv <视频链接> -P <保存目录>
 
以最好的画质与音频下载视频，加载cookies
yt-dlp -f ba+bv <视频链接> --cookies <cookies文件位置> -P <保存目录>
 
以最好的画质与音频下载youtube播放列表
yt-dlp -f 'bv*+ba' --download-archive videos.txt  https://www.youtube.com/playlist?list=****** -o '%(channel_id)s/%(playlist_id)s/%(id)s.%(ext)s'
 
以最好的画质与音频下载youtube某频道的所有公开内容，非公开需加载cookies文件
yt-dlp -f 'bv*+ba' --download-archive videos.txt https://www.youtube.com/@******/videos -o '%(channel)s/%(upload_date)s-%(title).200Bs.%(ext)s'
4 脚本下载
```

### 4 脚本下载

youtube上不少频道主由于被封号、下架视频等，导致我自己喜欢的视频常常找不到；故本博主喜欢将某些频道主视频进行onedrive备份，下面为下载脚本。可以实现：自动定时下载youtube指定频道内容；并且调用rclone上传到onedrive。

#### 4.1 脚本内容

```
#!/bin/bash
[[ ! -f "/home/yetpage" ]] && mkdir -p /home/yetpage
[[ ! -f "/home/log" ]] && mkdir -p /home/log
[[ ! -f "/home/yetpage/videotxt" ]] && mkdir -p /home/yetpage/videotxt
 
## 自定义文件下载主目录
cd /home/yetpage
 
## 指定下载频道
channels=(
    ## 下面为youtube频道主页链接，按照格式增加或者删减频道链接
    'https://www.youtube.com/@111/videos'
    'https://www.youtube.com/@222/videos'
    'https://www.youtube.com/@333/videos'
)
 
## 逐个下载视频，自动生成中文简体字幕并嵌入视频文件中
for channel in "${channels[@]}"; do
    /usr/bin/yt-dlp -f 'bv*+ba' \
    --download-archive videos.txt \
    --write-auto-sub --sub-format srt \
    --sub-lang zh-Hans --embed-sub \
    -i "$channel" \
    -o '%(channel)s/%(upload_date)s-%(id)s-%(title).200Bs.%(ext)s'
done
 
## 将下载视频id的记录保存到/home/yetpage/videotxt/videois.txt
cat videos.txt > /home/yetpage/videotxt/videois.txt
 
## rclone上传到网盘，不使用的直接注释下面代码，
## 指定rclone配置文件可添加参数: --config /home/yetpage/rclone.conf
/usr/bin/rclone move /home/yetpage 盘符:/yt \
-v --exclude "videos.txt" \
-P >> /home/log/yt-rclone.log 2>&1
 
## 说明一下
## --write-auto-sub 表示自动生成字幕。
## --write-sub 表示只下载存在的字幕文件
## --sub-format srt 表示字幕格式为 SRT 格式。
## --sub-lang zh-Hans 表示字幕语言为中文简体。
## --embed-sub 表示将生成的字幕嵌入到视频文件中。
## -i "$channel" 表示输入的视频文件路径或者链接地址是 $channel。
```

#### 4.2 部署脚本，定时执行

* 将脚本内容复制到/home/yt.sh文件
* 赋予脚本执行权限：  
  `chmod +x /home/yt.sh`
* crontab 每天6点定时执行脚本：  
  `0 6 * * * bash /home/yt.sh`

<script src="https://giscus.app/client.js"
	data-repo="tarenaexit/mkdocs-merterial-garden"
	data-repo-id="RR_kgDOL4wNPw"
	data-mapping="number"
	data-term="23"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
