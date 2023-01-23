---
title: windows samba命令行  
date: 2023-01-23 16:07  
tags: [samba]  
source: https://www.cnblogs.com/wangshaodong/p/16032362.html
---
## windows开启samba
1. 启用或关闭 Windows 功能
    - SMB 1.0/CIFS 文件共享支持
    - SMB 直通
2. 重启电脑

##  windows 命令行 配置samba
```powershell
# 查看所有 samba 连接
net use 
# 移除所有samba
net use /delete *
# 删除 z:盘映射
net use z: /delete
# 挂载samba共享为 z:盘
net use z: \\192.168.1.1\USB_disc1 /user:username passwd
```