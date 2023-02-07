---
title: snippet  
date: 2023-01-31 12:19:47  
tags: neovim  
---

```lua
vim.opt.runtimepath:append("/some/path/to/store/parsers")
```
```lua
if(vim.bo.filetype=="cpp") then
		vim.cmd("FloatermNew --autoclose=0 --position=bottomright g++ -g3 -std=c++2a -Wall %:p -o %:p:h/%:r && %:p:h/%:r && rm -f %:p:h/%:r")
	
```
```lua
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