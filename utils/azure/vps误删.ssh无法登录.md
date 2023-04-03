---
title: vps误删.ssh无法登录  
date: 2022-10-05 21:22:22  
tags: azure
---

## 情形:
- os: ubuntu
azure的vps默认禁用密码登录
再使用rsync同步文件时误删了家目录下所有文件
导致无法登录vps
<!-- more -->
## 解决办法
使用az工具(azure云终端或自己下载)
```bash
az vm user update \
  --resource-group myResourceGroup \
  --name myVM \
  --username azureuser \
  --ssh-key-value ~/.ssh/id_rsa.pub
```
[参考链接](https://learn.microsoft.com/zh-cn/azure/virtual-machines/extensions/vmaccess#code-try-0)