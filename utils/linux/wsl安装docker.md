---
title: wsl安装docker  
date: 2023-04-02 21:39  
tags:   
---

# wsl安装docker

## 问题
```bash
sudo apt update	
sudo apt upgrade
sudo apt install docker.io
```
如此方法安装docker会出现以下错误
```bash
$ sudo service docker start
docker: unrecognized service
```

## 解决方案
```bash
curl https://get.docker.com | sh
```