---
title: git submodule
date: 2023-02-07 15:19  
tags: [git submodule pull]  
source: https://blog.csdn.net/wkyseo/article/details/81589477
---
> 最近有个项目遇到有子模块，遂整理下。。牛逼的人感觉看官网就行，像我这种菜鸟总是需要反复记忆，[git官网链接戳此]。

## 1.先来个官方的API

```
git submodule [--quiet] add [<options>] [--] <repository> [<path>]
git submodule [--quiet] status [--cached] [--recursive] [--] [<path>…]
git submodule [--quiet] init [--] [<path>…]
git submodule [--quiet] deinit [-f|--force] (--all|[--] <path>…)
git submodule [--quiet] update [<options>] [--] [<path>…]
git submodule [--quiet] summary [<options>] [--] [<path>…]
git submodule [--quiet] foreach [--recursive] <command>
git submodule [--quiet] sync [--recursive] [--] [<path>…]
git submodule [--quiet] absorbgitdirs [--] [<path>…]
```

看完后其实也差不多明白了，比其他git命令多了个 `submodule` 关键字，先不看submodule命令，有submodule的仓库在当前目录会有个\*\*.gitmodules\*\*文件。记录path和url，如下。这里表明你引用的多少个子模块

```
[submodule "test"]
path = test
url = http://github.com/demo/test.git

```

还有一处改动在 `vi .git/config`查看，如下

```
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
        autocrlf=false
[remote "origin"]
        url = url....
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
[submodule "ssl"]
        active = true
        url = url....

```

上面的所有的命令基本都基于**此处两个文件的配置**来生效的。

## 2.解析git命令

常用命令如下

```
git clone <repository> --recursive  //递归的方式克隆整个项目
git submodule add <repository> <path> //添加子模块
git submodule init //初始化子模块
git submodule update //更新子模块
git submodule foreach git pull  //拉取所有子模块
```

### 2.1创建带子模块的版本库

例如我们要创建如下结构的项目

```
project
  |--moduleA
  |--readme.txt
```

创建project版本库，并提交readme.txt文件

```
git init --bare project.git
git clone project.git 
cd project1
echo "This is a project." > readme.txt
git add *
git commit -m "add readme.txt"
git push origin master
cd ..
```

创建moduleA版本库，并提交a.txt文件

```
git init --bare moduleA.git
git clone moduleA.git 
cd moduleA1
echo "This is a submodule." > a.txt
git add *
git commit -m "add a.txt"
git push origin master
```

在project项目中引入子模块moduleA，并提交子模块信息

```
cd project1
git submodule add ../moduleA.git moduleA
git status
git diff
git add*
git commit -m "add submodule"
git push origin master
```

使用git status可以看到多了两个需要提交的文件，其中.gitmodules指定submodule的主要信息，包括子模块的路径和地址信息，moduleA指定了子模块的commit id，使用git diff可以看到这两项的内容。这里需要指出**父项目的git并不会记录submodule的文件变动，它是按照commit id指定submodule的git header**，所以.gitmodules和moduleA这两项是需要提交到父项目的远程仓库的。

```
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
    new file:   .gitmodules
    new file:   moduleA
```

###2.2 克隆带子模块的版本库  
方法一，先clone父项目，再初始化submodule，最后更新submodule，初始化只需要做一次，之后每次只需要直接update就可以了，需要注意submodule默认是不在任何分支上的，它指向父项目存储的submodule commit id。

```
git clone project.git project2
cd project2
git submodule init
git submodule update
```

方法二，采用递归参数–recursive，需要注意同样submodule默认是不在任何分支上的，它指向父项目存储的submodule commit id。

```
git clone project.git project3 --recursive
```

### 2.3修改子模块

修改子模块之后只对子模块的版本库产生影响，对父项目的版本库不会产生任何影响，如果父项目需要用到最新的子模块代码，我们需要更新父项目中submodule commit id，默认的我们使用git status就可以看到父项目中submodule commit id已经改变了，我们只需要再次提交就可以了。

```
cd project1/moduleA
git branch
echo "This is a submodule." > b.txt
git add *
git commit -m "add b.txt"
git push origin master
cd ..
git status
git diff
git add *
git commit -m "update submodule add b.txt"
git push origin master
```

### 2.4更新子模块

更新子模块的时候要注意子模块的分支默认不是master。

方法一，先pull父项目，然后执行git submodule update，注意moduleA的分支始终不是master。

```
cd project2
git pull
git submodule update
```

方法二，先进入子模块，然后切换到需要的分支，这里是master分支，然后对子模块pull，这种方法会改变子模块的分支。

```
cd project3/moduleA
git checkout master
cd ..
git submodule foreach git pull
```

5.  删除子模块  
    网上有好多用的是下面这种方法

```
git rm --cached moduleA
rm -rf moduleA
rm .gitmodules
vim .git/config
```

删除submodule相关的内容，例如下面的内容

```
[submodule "moduleA"]
      url = /Users/nick/dev/nick-doc/testGitSubmodule/moduleA.git
```

然后提交到远程服务器

```
git add .
git commit -m "remove submodule"
```

但是我自己本地实验的时候，发现用下面的方式也可以，服务器记录的是.gitmodules和moduleA，本地只要用git的删除命令删除moduleA，再用git status查看状态就会发现.gitmodules和moduleA这两项都已经改变了，至于.git/config，仍会记录submodule信息，但是本地使用也没发现有什么影响，如果重新从服务器克隆则.git/config中不会有submodule信息。

```
git rm moduleA
git status
git commit -m "remove submodule"
git push origin master
```

## 3.问题

![这里写图片描述][fig2]  
`git submodule update`出现此问题，是因为终端用的不是windows自带的cmd，用自带的cmd打开执行此命令即可

我的博客即将同步至腾讯云+社区，邀请大家一同入驻：[https://cloud.tencent.com/developer/support-plan?invite\_code=14ti7um6gsjlj]

[fig1]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png
[fig2]: https://img-blog.csdn.net/20180812145104692?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dreXNlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70

[git官网链接戳此]: https://git-scm.com/docs/git-submodule
[https://cloud.tencent.com/developer/support-plan?invite\_code=14ti7um6gsjlj]: https://cloud.tencent.com/developer/support-plan?invite_code=14ti7um6gsjlj
