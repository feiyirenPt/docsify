---
title: revealjs制作ppt  
date: 2023-02-07 00:14  
tags:   
---

# revealjs制作ppt

## installation

1. [Full Setup](https://revealjs.com/installation/#full-setup) (`Recommended`)
- setup
    ```bash
    git clone https://github.com/hakimel/reveal.js.git
    cd reveal.js && npm install
    npm start
    ```
- Open http://localhost:8000 to view your presentation

- [Development Server Port](https://revealjs.com/installation/#development-server-port) 

切换端口
```bash
npm start -- --port=8001
```

2. [Installing From npm](https://revealjs.com/installation/#installing-from-npm)


### 问题
- 遇到PUPPETEER_SKIP_CHROMIUM_DOWNLOAD报错
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
然后npm i
或者
```bash
npm config set puppeteer_download_host=https://npm.taobao.org/mirrors
npm i puppeteer
```

## reference
-[reveal.js](https://revealjs.com/)