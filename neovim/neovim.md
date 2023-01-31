---
title: neovim
date: 2022-12-21 20:32:47  
tags: neovim  
---

## 常用模块
-   `vim.{o/wo/bo}`: vim 选项，例如 `:lua vim.wo.number = true` 等价于 `:set number`
-   `vim.g`：全局变量，相当于 `set g:variable = value`
-   `vim.env`: 访问和配置环境变量
-   `vim.fn`: 访问 vim 运行时函数，例如 `:lua print(vim.fn.getenv('HOME'))` 等价于 `:echo getenv('HOME')` 写法
-   `vim.api`: 提供了一些 api 代替 vim 命令，例如不严格来说，vim 中的 map 对应 `vim.api.nvim_set_keymap`
-   `vim.cmd`: 在 lua 中执行 vimscript，例如 `:lua vim.cmd('echo getenv("HOME")')`
-   `vim.lsp`: 提供了 lsp 相关的功能，例如：`:lua vim.lsp.buf.formatting()`
-   `vim.inspect`: 可以把 vim 运行时对象转成可以打印的 lua 对象格式，例如 `lua print(vim.inspect(vim.opt.completeopt))`


## o/wo/bo 和 opt
vim 中有 3 种范围的选项：global、window-local、buffer-local，在旧版(vimscript 版)里，统一使用 `set <option> [ = value ]` 语法设置，新版改用带范围的 o/wo/bo 设置选项，并且使用布尔值代替了 `no*` 选项，并且 nvim 还提供了一种配置方法，那就是 `vim.opt`，opt 的写法比较像旧版的 set，

## reference
- neovim lua配置: [Neovim Lua Config  vizee](https://vizee.org/2022/04/03/neovim-lua-config)
- 如何写插件: [A Basic Lua Plugin  Scripting Neovim with Lua](https://jacobsimpson.github.io/nvim-lua-manual/docs/basic-plugin/)
- 如何写自己的statusline [How I made my Neovim statusline in Lua  Elianiva](https://elianiva.my.id/post/neovim-lua-statusline/)