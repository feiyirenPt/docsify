---
title: windowsVPS安装openssh
date: 2022-10-06 13:06:22
tags: azure
categories: coding
---

- 查看ssh
```powershell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```
## 高版本windows server
- 安装
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```
[参考资料](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse)

## 低版本windows server
先安装scoop
遇到`powershell 请求被中止: 未能创建 SSL/TLS 安全通道`眼原因协议问题, 解决方法[`Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\.NetFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value '1' -Type DWord`适用32位](https://www.jianshu.com/p/755bea273e95)
```powershell
scoop install sudo openssh
最后根据提示把openssh注册为服务
最后失败...
```

## 最后
### Start the sshd service
Start-Service sshd
### OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

### 关闭防火墙
```powershell
Set-NetFirewallProfile -Profile Private -Enabled False
Set-NetFirewallProfile -Profile Public -Enabled False
Get-NetFirewallProfile
```