---
title: 2步搭建个人RSSHub，订阅不支持RSS的网站  
date: 2023-01-11 17:30  
tags: [RSS]  
source: https://zhuanlan.zhihu.com/p/395100455
---
RSS，是很古老的产物；在现在已经很少有人使用了。

**那么为啥我现在还在坚持使用RSS呢？**

> 因为我不想被推荐算法洗脑壳……还有就是，我比较懒；只想在一个位置看抖音、微博、贴吧、微信里面的文章/视频，不想打开几个APP。

如果你对RSS这个东西很迷惑，那么推荐你先看看这两篇文章：

![][fig1]

**RSSHub**是一个开源、简单易用、易于扩展的 **RSS 生成器**，可以给任何奇奇怪怪的内容生成 **RSS 订阅源**。**它可以为一些不提供Rss源的网站生成适配Rss地址**

现在RSSHub反爬越来越严格了，还有就是RSSHub在国内已经不能使用…所以只有搭建个人RSSHub这一条路了。

## **二、搭建个人RSShub**

## **推荐：部署到Heroku(免费)**

**1、注册Heroku账户**

进入[官网]，随意注册一个用户名就行了！

看不懂英文，推荐edge/chrome浏览器都自带翻译！

![][fig2]

**2、安装RSSHub**

直接点击[部署]，会自动部署，对于小白玩家极其实用！

![][fig3]

除了“App name”之外，其他都不用修改；最后点击“Deploy app”即可！

## **其他部署方法**

-   Docker
-   腾讯云
-   ……

这些要不需要付费，要不就是比较麻烦!

## **懒人必备**

如果不想去费时间搭建RSSHub，那么可以直接使用别人搭建好的。

-   [https://rss.shab.fun/]
-   [https://rss.injahow.cn/]
-   [http://i.scnu.edu.cn/sub]



[官网]: https://link.zhihu.com/?target=https%3A//dashboard.heroku.com/
[部署]: https://link.zhihu.com/?target=https%3A//heroku.com/deploy%3Ftemplate%3Dhttps%253A%252F%252Fgithub.com%252FDIYgod%252FRSSHub
[https://rss.shab.fun/]: https://rss.shab.fun/
[https://rss.injahow.cn/]: https://rss.injahow.cn/
[http://i.scnu.edu.cn/sub]: https://i.scnu.edu.cn/sub


[fig1]: https://pic2.zhimg.com/v2-64231d1b343eb603727960456860554d_b.jpg
[fig2]: https://pic4.zhimg.com/v2-6b009355a97fc747bb6d7d9aa9ccaadf_b.jpg
[fig3]: https://pic1.zhimg.com/v2-4d94e3106c7de1da1913f20706afc6cc_b.jpg