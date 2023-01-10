---
title: video
date: 2022-10-29 23:40:31
tags: web
categories: coding
---
[ 在html中插入图片和视频 ](https://blog.csdn.net/weixin_44093867/article/details/104166514)

```html
<iframe src="（视频网址）" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%"  height="580" quality="high" > </iframe>

```
```html
<div style="position: relative; width: 100%; height: 0; padding-bottom: 75%;"><iframe 
src="//player.bilibili.com/player.html?aid=39807850&cid=69927212&page=1" scrolling="no" border="0" 
frameborder="no" framespacing="0" allowfullscreen="true" style="position: absolute; width: 100%; 
height: 100%; left: 0; top: 0;"> </iframe></div>
```

[iframe中视频无法自动播放](https://zhuanlan.zhihu.com/p/537872435)
使用`allow="autoplay"`解决