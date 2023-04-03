---
title: 用 git filter-repo 彻底删除Git中的大文件
date: 2023-01-19 23:47:34  
tags: git
source: https://www.jianshu.com/p/03bf1bc1b543
---

```bash
pip install git-filter-repo
```

## 用 git filter-repo 彻底删除Git中的大文件

## Intro

网上能搜到的资料大部分都是 git filter-branch，不仅速度慢，还容易出问题，而且官方都在使用git filter-branch时推荐git filter-repo，因此尝试一下官方推荐的方法

## 安装git-filter-repo

[官方Git库有很详细的说明]

```bash
pip install git-filter-repo
```

## 找出要删除的大文件

按照文件大小升序排列并取最后40个文件

```bash
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -40 | awk '{print$1}')"
```

注意嵌套语句会导致排序错乱，可以拆开逐个寻找文件

```bash
git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -40
git rev-list --objects --all | grep 文件对应的id
```

## 彻底删除大文件

[官方文档列出了各种功能，在此就不一一展示了]

由于本人不小心上传了大量csv文件，因此使用正则匹配将所有csv文件删除

```bash
git filter-repo --force --invert-paths --path-regex .+\.csv
```

## 强制推送

由于修改了历史的commit，因此仓库无法正常推送到远端，需要进行强制推送

```bash
git push -f origin master
```

[官方Git库有很详细的说明]: https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fnewren%2Fgit-filter-repo%2Fblob%2Fmain%2FINSTALL.md
[官方文档列出了各种功能，在此就不一一展示了]: https://links.jianshu.com/go?to=https%3A%2F%2Fhtmlpreview.github.io%2F%3Fhttps%3A%2F%2Fgithub.com%2Fnewren%2Fgit-filter-repo%2Fblob%2Fdocs%2Fhtml%2Fgit-filter-repo.html
