---
title: neovim的文件结构
date: 2022-12-21 20:32:47
tags: neovim
categories: neovim
---

## neovim
- neovim是vim8的fork版本
- neovim是现代化的编辑器,作为我的主力编辑器
- neovim使用lua做配置,兼容vimscript

## 配置目录
```
~\AppData\Local\nvim
├───ftplugin       -- 针对每种语言的配置  
|   ├─── json.lua
|   ├─── python.lua
|   ├─── tex.lua
|   └───text.lua
├───lua
│   ├───basic      -- 针对neovim的设置
│   |   ├─── autocmd.lua
│   |   ├─── keybinds.lua
│   |   ├─── plugins.lua
│   |   └─── settings.lua
│   └───conf       -- 针对每种插件设置
│       ├─── coc.lua
│       ├─── ...
│       └─── ...
├───init.lua       -- neovim启动后加载的文件
└───plugin         -- 插件管理器packer的缓存目录
```
