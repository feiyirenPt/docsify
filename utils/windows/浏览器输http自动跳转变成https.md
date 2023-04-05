---
title: 浏览器输入http被自动跳转至https问题  
date: 2023-04-04 12:10  
tags: [http页面用window.open跳转为什么会变成https]  
source: https://blog.csdn.net/trsl_programmer/article/details/122165145  
---

## 问题

在将服务尝试着从http协议往https协议迁移成功之后，又出于测试调试的目的将服务转回到http协议，却发现在浏览器输入http会被自动跳转到https。

> HTTP Strict Transport Security (HSTS) is an opt-in security enhancement that is specified by a web application through the use of a special response header. Once a supported browser receives this header that browser will prevent any communications from being sent over HTTP to the specified domain and will instead send all communications over HTTPS. It also prevents HTTPS click through prompts on browsers.

查阅相关资料，发现这是浏览器的HSTS（HTTP Strict Transport Security）功能引起的。在安装配置SSL证书时，可以使用一种能使数据传输更加安全的Web安全协议，即在服务器端上开启HSTS ，它会告诉浏览器只能通过HTTPS访问，而绝对禁止HTTP方式。

因此，只要关闭浏览器的HSTS功能就可以解决这个问题，但是只能通过特定的方式，而不是清除浏览器缓存那么简单。

## 解决方案

### Chrome浏览器
1. 地址栏中输入chrome://net-internals/#hsts。
2. 在Delete domain中输入项目的域名，并Delete（删除）`。`
3. 可以在Query domain测试是否删除成功。

## Opera浏览器

和Chrome方法一样。

### Safari浏览器

1. 完全关闭Safari浏览器。
2. 删除~/Library/Cookies/HSTS.plist这个文件。
3. 重新打开Safari即可（极少数情况下，可能需要重启系统）。

### Firefox浏览器

1. 关闭所有已打开的页面。
2. 清空历史记录和缓存。
3. 地址栏输入about:permissions。
4. 搜索项目域名，并点击Forget About This Site。
