---
title: git创建一个空白新分支
date: 2023-02-07 14:47  
tags: [git]  
source: https://blog.csdn.net/zs634134578/article/details/9183705
---
### 1 创建一个分支

使用参数 --orphan，这个参数的主要作用有两个，一个是拷贝当前所在分支的所有文件，另一个是没有父结点，可以理解为没有历史记录，是一个完全独立背景干净的分支。

参考git的帮助文档，如下：

![][fig1]  

```bash
$ git checkout --orphan gh-pages
# 创建一个orphan的分支，这个分支是独立的
Switched to a new branch 'gh-pages'
```

### 2 清空当前分支下的所有文件

这个操作不会影响别的分支，特别是你的<start point>

```
git rm -rf .
# 删除原来代码树下的所有文件
```

![][fig2]  

  

### 3 这时候是看不到当前分支的

使用命令：

```
git branch -a
```

![][fig3]

不用紧张，只要执行commit命令后就能看到了。

```
git commit -am "xxx"
```

![][fig4]

### 参考：

git帮助文档

《在git下创建一个空分支》    [http://www.ooso.net/archives/636]  

  

[fig1]: https://img-blog.csdn.net/20130627005032500?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvenM2MzQxMzQ1Nzg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center
[fig2]: https://img-blog.csdn.net/20130627005836843?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvenM2MzQxMzQ1Nzg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center
[fig3]: https://img-blog.csdn.net/20130627010030625?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvenM2MzQxMzQ1Nzg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center
[fig4]: https://img-blog.csdn.net/20130627010327093?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvenM2MzQxMzQ1Nzg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center

[http://www.ooso.net/archives/636]: http://www.ooso.net/archives/636
