---
title: ffmpeg视频转码
date: 2022-10-29 23:23:31
tags: ffmpeg opencv
categories: coding
---

视频编码格式为 H264
```
ffmpeg -i input.mp4 -vcodec h264 output.mp4  
```
[视频转码 转H264格式](https://blog.csdn.net/flyfor2013/article/details/115529167)

html的video标签只能播放H264的mp4视频


ffmpeg查看视频信息 `ffprobe file.mp4 -show_streams -select_streams v -print_format json` 

