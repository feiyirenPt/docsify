---
title: neovim的文件结构  
date: 2022-12-21 20:32:47  
tags: neovim  
source: https://vizee.org/2022/04/03/neovim-lua-config/#%E6%96%B0%E9%85%8D%E7%BD%AE%E4%BB%8B%E7%BB%8D
---

## some snippets
```lua
vim.opt.runtimepath:append("/some/path/to/store/parsers")

if(vim.bo.filetype=="cpp") then
		vim.cmd("FloatermNew --autoclose=0 --position=bottomright g++ -g3 -std=c++2a -Wall %:p -o %:p:h/%:r && %:p:h/%:r && rm -f %:p:h/%:r")
	
function M.down()
    local timer = vim.loop.new_timer()
    local stop = false
    local sleep = 5000
    timer:start(1000, sleep, vim.schedule_wrap(function()
      local scroll_down = vim.api.nvim_replace_termcodes('normal <C-E>', true, true, true)
      vim.cmd(scroll_down)

      if stop then
        timer:close()
      end
    end))
end
```

```lua
-- 修改lua/plugins.lua 自动更新插件
autocmd("BufWritePost", {
	group = myAutoGroup,
	-- autocmd BufWritePost plugins.lua source <afile> | PackerSync
	callback = function()
		if vim.fn.expand("<afile>") == "lua/plugins.lua" then
			vim.api.nvim_command("source lua/plugins.lua")
			vim.api.nvim_command("PackerSync")
		end
	end,

    -- nvim-tree 自动关闭
autocmd("BufEnter", {
	nested = true,
	group = myAutoGroup,
	callback = function()
		if #vim.api.nvim_list_wins() == 1 and vim.api.nvim_buf_get_name(0):match("NvimTree_") ~= nil then
			vim.cmd("quit")
		end
	end,
})

```


## 常用模块

-   `vim.{o/wo/bo}`: vim 选项，例如 `:lua vim.wo.number = true` 等价于 `:set number`
-   `vim.g`：全局变量，相当于 `set g:variable = value`
-   `vim.env`: 访问和配置环境变量
-   `vim.fn`: 访问 vim 运行时函数，例如 `:lua print(vim.fn.getenv('HOME'))` 等价于 `:echo getenv('HOME')` 写法
-   `vim.api`: 提供了一些 api 代替 vim 命令，例如不严格来说，vim 中的 map 对应 `vim.api.nvim_set_keymap`
-   `vim.cmd`: 在 lua 中执行 vimscript，例如 `:lua vim.cmd('echo getenv("HOME")')`
-   `vim.lsp`: 提供了 lsp 相关的功能，例如：`:lua vim.lsp.buf.formatting()`
-   `vim.inspect`: 可以把 vim 运行时对象转成可以打印的 lua 对象格式，例如 `lua print(vim.inspect(vim.opt.completeopt))`

其他没写到的都是因为我没怎么用到。

## o/wo/bo 和 opt

vim 中有 3 种范围的选项：global、window-local、buffer-local，在旧版(vimscript 版)里，统一使用 `set <option> [ = value ]` 语法设置，新版改用带范围的 o/wo/bo 设置选项，并且使用布尔值代替了 `no*` 选项，并且 nvim 还提供了一种配置方法，那就是 `vim.opt`，opt 的写法比较像旧版的 set，


## reference

- 如何写插件: [A Basic Lua Plugin  Scripting Neovim with Lua](https://jacobsimpson.github.io/nvim-lua-manual/docs/basic-plugin/)

- 如何写自己的statusline [How I made my Neovim statusline in Lua  Elianiva](https://elianiva.my.id/post/neovim-lua-statusline/)