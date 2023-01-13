---
title: ffmpeg视频转码  
date: 2022-10-29 23:23:31  
tags: ffmpeg opencv  
---

## ffmpeg查看视频信息 
`ffprobe file.mp4 -show_streams -select_streams v -print_format json` 

## 视频编码格式为 H264
```
ffmpeg -i input.mp4 -vcodec h264 output.mp4  
```
[视频转码 转H264格式](https://blog.csdn.net/flyfor2013/article/details/115529167)

html的video标签只能播放H264的mp4视频

## ffmpeg合并视屏

这种方法成功率很高，也是最好的，但是需要 FFmpeg 1.1 以上版本。先创建一个文本文件 filelist.txt：

```txt
file 'input1.mkv' 
file 'input2.mkv'
file 'input3.mkv'
```

```cmd
ffmpeg -f concat -i filelist.txt -c copy output.mkv
```

注意：使用 FFmpeg concat 分离器时，如果文件名有奇怪的字符，要在  filelist.txt 中转义。


## reference
[使用ffmpeg合并视频文件的三种方法](https://blog.csdn.net/u012587637/article/details/51670975)