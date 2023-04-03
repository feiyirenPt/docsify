---
title: GitHub 通过 jsdelivr CDN加持
date: 2023-02-03 18:59  
tags: [github,cdn,jsdelivr]  
source: https://www.cnblogs.com/qqlcx5/p/13299120.html
---

## GitHub 通过 jsdelivr CDN加持

两种引用方式：
-   存入仓库分支里面，直接引用
-   创建版本号后，在引用

### 直接引用
格式为：
```
https://cdn.jsdelivr.net/gh/<用户名>/<仓库名>/<文件及路径>
```

例：
```
GitHub
https://github.com/qqlcx5/figure-bed/blob/master/img/20200710230327.jpg
转成 jsdelivr
https://cdn.jsdelivr.net/gh/qqlcx5/figure-bed/img/20200710230327.jpg
```
总结：

```
github.com`替换成cdn.jsdelivr.net/gh

/blob/master 删除
```

### 版本号

版本号用@符链接。格式：

```
https://cdn.jsdelivr.net/gh/<用户名>/<仓库名>@[版本号]/<文件及路径>
```
例：
```
GitHub
https://github.com/qqlcx5/figure-bed/blob/1.0/img/20200710230327.jpg
转成 jsdelivr
https://cdn.jsdelivr.net/gh/qqlcx5/figure-bed@1.0/img/20200710230327.jpg
```

总结：
```
github.com`替换成cdn.jsdelivr.net/gh

/blob/ 替换成 @ 
注：1.0 创建的版本号
```

已发布的版本不会受到仓库内容变化的影响  
如何按版本号引用。链接相对稳定.



## 突破 Jsdelivr 50M 上限
- 为了能免费撸羊,使用发布版本号方案，只要单次版本号的大小不超过50M即可，多次版本号就可以突破50M限制。
- `添加 @master`  
原CDN链接:`https://cdn.jsdelivr.net/gh/Borber/PublicPic1/Date/20200810/2.jpg`  
加上之后:`https://cdn.jsdelivr.net/gh/Borber/PublicPic1@master/Date/20200810/2.jpg`