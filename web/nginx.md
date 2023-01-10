---
title: nginx
date: 2022-12-1 22:40:31
tags: nginx
categories: coding
---
-nginx响应类型default_type:

Nginx 会根据mime type定义的对应关系来告诉浏览器如何处理服务器传给浏览器的这个文件，是打开还是下载
如果Web程序没设置，Nginx也没对应文件的扩展名，就用Nginx 里默认的 default_type定义的处理方式。
default_type application/octet-stream; #nginx默认文件类型

config:
<!-- more -->

```conf
user root;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##

	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;

	server {
			listen 5000 ssl;
			server_name localhost;
			ssl_protocols TLSv1.2 TLSv1.1 TLSv1;
			ssl_certificate      /etc/nginx/cert/server.pem;
			ssl_certificate_key  /etc/nginx/cert/private_unsecure.key;
			ssl_prefer_server_ciphers on;
			location / {
			  proxy_pass http://127.0.0.1:5230/;
			  client_max_body_size 20000m;
			  proxy_set_header Host      $host;
			  proxy_set_header X-Real-IP $remote_addr;
		  }
	}

	server {
		listen 80;
		location / {
            root   html;
            index  index.html index.htm;
            gzip_static on;
        }
		
	}

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

		location /memos/ {
			alias /var/www/memos/;
			index index.html index.htm;
		}
		location /jyf/ {
			  return 301 https://www.wycjyf.live:5000;
		}

		location /alist/ {
			  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			  proxy_set_header Host $http_host;
			  proxy_set_header X-Real-IP $remote_addr;
			  proxy_set_header Range $http_range;
			  proxy_set_header If-Range $http_if_range;
			  proxy_redirect off;
			  proxy_pass https://www.wycjyf.live/football;
			  # the max size of file to upload
			  client_max_body_size 20000m;
		}

		location /football/ {
			  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			  proxy_set_header Host $http_host;
			  proxy_set_header X-Real-IP $remote_addr;
			  proxy_set_header Range $http_range;
			  proxy_set_header If-Range $http_if_range;
			  proxy_redirect off;
			  proxy_pass http://127.0.0.1:5244/;
			  # the max size of file to upload
			  client_max_body_size 20000m;
		}
	}
}


#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
# 
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
# 
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
# 
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}
```