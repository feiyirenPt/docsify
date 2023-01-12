---
title: nginx  
date: 2022-12-1 22:40:31  
tags: nginx  
---
- nginx响应类型default_type:

Nginx 会根据mime type定义的对应关系来告诉浏览器如何处理服务器传给浏览器的这个文件，是打开还是下载
如果Web程序没设置，Nginx也没对应文件的扩展名，就用Nginx 里默认的 default_type定义的处理方式。 
`default_type application/octet-stream;` #nginx默认文件类型

config:

```conf
http {
    server {
		listen 443 ssl;
		server_name localhost;
		ssl_protocols TLSv1.2 TLSv1.1 TLSv1;
		ssl_certificate      /etc/nginx/cert/server.pem;
		ssl_certificate_key  /etc/nginx/cert/private_unsecure.key;
		ssl_prefer_server_ciphers on;

		location / {
			default_type text/html;
			root /var/www/hexo;
			index index.html index.htm;
		}
	}
```

`$request_filename`判断文件  
[?代表懒惰模式正则][lk1]
```conf
if ($request_filename ~* ^.*?\.(html|doc|pdf|zip|docx|txt)$) {
    add_header Content-Disposition attachment;
    add_header Content-Type application/octet-stream;
}
```


## reference
- [nginx全局变量和正则匹配](https://www.cnblogs.com/robinunix/p/12843815.html)
- [lk1]: https://blog.csdn.net/zth1002/article/details/44131165