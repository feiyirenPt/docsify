---
title: 无法ssh密码登录azureVPS  
date: 2023-03-22 23:28  
tags:   
---

# 无法ssh密码登录azureVPS

## 问题
已经确保
```bash
PermitRootLogin yes
PasswordAuthentication yes
```
可以通过key登录,但是死活不能通过密码登录


## 解决方案
在`sshd_config`第12行左右有
```bash
Include /etc/ssh/sshd_config.d/*.conf
```
`sshd_config.d/`目录下
```bash
jyf@ubuntu:/etc/ssh/sshd_config.d$ ls
50-cloud-init.conf  50-cloudimg-settings.conf
```

```bash
jyf@ubuntu:/etc/ssh/sshd_config.d$ sudo cat 50-cloud-init.conf
PasswordAuthentication no
```

```bash
jyf@ubuntu:/etc/ssh/sshd_config.d$ sudo cat 50-cloudimg-settings.conf
# CLOUD_IMG: This file was created/modified by the Cloud Image build process

# Keep alive ssh connections by sending a packet every 2 minutes.
ClientAliveInterval 120
```

自带的openssh夹带私货,把Include注释掉