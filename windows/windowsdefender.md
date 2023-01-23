---
title: Windows Defender  
date: 2022-10-9  
tags: [defender,path]  
---
1. - 通过注册表命令方式来 禁止Windows Defender开机自动运行和彻底关闭它.
   
   - 先关闭Windows Defender的防篡改功能，再以管理员身份运行PowerShell或命令提示符CMD，然后输入：
   
   - 禁用：reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /d 1 /t REG_DWORD /f
   
   - 恢复：reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware"

2. windows path 只要有一个为空后面就无效了

3. MSVC用以前版本编译项目注意SDK和MSVC版本
