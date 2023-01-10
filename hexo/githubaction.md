---
title: github action上传服务器失败
date: 2022-10-13 20:49:45
tags: github
categories: coding
---

# github action 执行中报错 Invalid key format

本来以为是[ssh 密钥文件格式不兼容的问题](https://github.com/wlixcc/SFTP-Deploy-Action/issues/1),后来发现 secrets 不能放在 `repo > settings > secrets > Environment secrets` 里面,要放在 `repo > settings > actions > secrets > Repository secrets` 里面,原回答参考
[github secret key](https://github.com/wlixcc/SFTP-Deploy-Action/issues/1#issuecomment-1073142210)

<details>
<summary>deploy.yml</summary>

```yml
name: Hexo Deploy

on:
  push:
    branches:
      - master

jobs:
  build:
    runs-on: ubuntu-latest
    if: github.event.repository.owner.id == github.event.sender.id

    steps:
      - name: Checkout source
        uses: actions/checkout@v3
        with:
          ref: master

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: latest

      - name: Setup Hexo
        env:
          ACTION_DEPLOY_KEY: ${{ secrets.HEXO_DEPLOY_KEY }}
        run: |
          mkdir -p ~/.ssh/
          echo "$ACTION_DEPLOY_KEY" > ~/.ssh/id_rsa
          chmod 700 ~/.ssh
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan 20.239.182.249 >> ~/.ssh/known_hosts
          git config --global user.email "jyfserendipity@outlook.com"
          git config --global user.name "jyf-111"
          npm install hexo-cli -g
          npm install

      - name: Deploy
        run: |
          hexo clean
          hexo generate
          hexo deploy
```

</details>
