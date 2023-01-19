---
title: proxy  
date: 2022-10-12  
tags: [ proxy,sock5,pppoe ]
---
## 拨号上网相关

inetcpl
rasdial
- 拨号上网挂代理只能设置网络连接为英文名  

## 终端代理

- [使用 sock5代理]( https://www.jianshu.com/p/1c37903dd09d )
```cmd
set https_proxy=socks://127.0.0.1:10809
set http_proxy=socks://127.0.0.1:10809
```
```powershell
$env:HTTP_PROXY="socks://127.0.0.1:10809"
$env:HTTPS_PROXY="socks://127.0.0.1:10809"
```
<!--more-->
- [电信光猫获取超级密码](https://www.jianshu.com/p/bdc2b115f09e)

## uwp代理

- UWP去除网络隔离实现代理 powershell 执行 
```powershell
foreach ($n in (get-appxpackage).packagefamilyname) {checknetisolation loopbackexempt -a -n="$n"}
```
## github代理
- ineo6/hosts
- gitclone.com： https://gitclone.com/  
- Github 仓库加速： https://github.zhlh6.cn/  
- https://ghproxy.com/
- https://gh.api.99988866.xyz
- https://gh.con.sh
- https://gh.ddlc.top
- https://gh2.yanqishui.work
- https://ghdl.feizhuqwq.cf
- https://ghproxy.com
- https://ghps.cc
- https://git.xfj0.cn
- https://github.91chi.fun
- https://proxy.zyun.vip