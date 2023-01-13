---
title: Docker快速搭建Miniflux+RSSHub
date: 2023-01-13 10:32  
tags: [MiniFlux,RSS,RSSHub]  
source: https://www.jkg.tw/p3246/
---



# 安装Miniflux +RSSHub
## 两个服务写在一个`docker-compose.yaml`里面

```yaml
version: "3"

services:

   miniflux:
     image: miniflux/miniflux:latest
     container_name: miniflux
     restart: unless-stopped
     ports:
       - "8888:8080"
     depends_on:
       - db
       - rsshub
     environment:
       - DATABASE_URL=postgres://miniflux:somepass888@db/miniflux?sslmode=disable
       - POLLING_FREQUENCY=15
       - RUN_MIGRATIONS=1

   db:
     image: postgres:latest
     container_name: postgres
     restart: unless-stopped
     environment:
       - POSTGRES_USER=miniflux
       - POSTGRES_PASSWORD=7788
     volumes:
       - miniflux-db:/var/lib/postgresql/data

   rsshub:
     image: diygod/rsshub:latest
     container_name: rsshub
     restart: unless-stopped
     ports:
       - "1200:1200"
     environment:
       NODE_ENV: production
       CACHE_TYPE: redis
       REDIS_URL: "redis://redis:6379/"
       PUPPETEER_WS_ENDPOINT: "ws://browserless:3000"
     depends_on:
       - redis
       - browserless

   browserless:
     image: browserless/chrome:latest
     container_name: browserless
     restart: unless-stopped

   redis:
     image: redis:alpine
     container_name: redis
     restart: unless-stopped
     volumes:
       - redis-data:/data

volumes:
  miniflux-db:
  redis-data:
```


## 还需要下面两条指令初始化Miniflux数据库
```bash
# 下面這條指令在日後 Miniflux 大版本升級時候有可能也會用到
docker-compose exec miniflux /usr/bin/miniflux -migrate
# 下面這條在新增管理員帳號跟密碼，等下要登入 Miniflux 管理後台用的
docker-compose exec miniflux /usr/bin/miniflux -create-admin
```

完成以上指令就完成全部安装，只要打开浏览器输入服务器 IP 加上端口 8888 即可进入 Miniflux 网页

![][fig1]

👆 Miniflux 登入画面

Miniflux 真的轻巧，登录画面极度简约，只有帐号、密码以及 Login 按钮，连个 logo 都没有 👍

以上全部设定完毕后，即可安全的使用你的专属域名打开你专属的 RSS 阅读器


## reference
- [miniflux的docker-compose.yaml](https://raw.githubusercontent.com/DIYgod/RSSHub/master/docker-compose.yml)



[fig1]: https://www.jkg.tw/media/2020/03/CleanShot-2020-03-06-at-11.12.55-20200317181631596.png#little