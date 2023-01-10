title: proxy
date: 2022-10-12
tags:
- proxy
- sock5
- pppoe
categories: [ computer ]
---

inetcpl
rasdial
- 拨号上网挂代理只能设置网络连接为英文名  
https://www.jianshu.com/p/1c37903dd09d
- 使用sock5代理
```cmd
set https_proxy=socks://127.0.0.1:10809
set http_proxy=socks://127.0.0.1:10809
```
```powershell
$env:HTTP_PROXY="socks://127.0.0.1:10809"
$env:HTTPS_PROXY="socks://127.0.0.1:10809"
```
<!--more-->
- 电信光猫获取超级密码](https://www.jianshu.com/p/bdc2b115f09e)

- UWP去除网络隔离实现代理 powershell 执行 
```powershell
foreach ($n in (get-appxpackage).packagefamilyname) {checknetisolation loopbackexempt -a -n="$n"}
```
github ineo6/hosts

hub.fastgit.xyz