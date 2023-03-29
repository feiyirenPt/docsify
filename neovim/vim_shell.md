---
title: vim设置shell
date: 2023-1-15 23:52:09  
tags: neovim  
---

## powershell
```lua
local powershell_options = {
	shell = vim.fn.executable "pwsh" and "pwsh" or "powershell",
	shellcmdflag = "-NoLogo -NoProfile -ExecutionPolicy RemoteSigned -Command [Console]::InputEncoding=[Console]::OutputEncoding=[System.Text.Encoding]::UTF8;",
	shellredir = "-RedirectStandardOutput %s -NoNewWindow -Wait",
	shellpipe = "2>&1 | Out-File -Encoding UTF8 %s; exit $LastExitCode",
	shellquote = "",
	shellxquote = "",
}

if vim.fn.has('win32') == 1 and vim.fn.has("linux") == 0 then
	for option, value in pairs(powershell_options) do
		vim.opt[option] = value
	end
end
```

## git-bash
```lua
vim.o.shell = "C:/Users/jyf/scoop/apps/git/current/bin/bash.exe"
vim.o.shellcmdflag = "-c"
vim.o.shellredir = ">%s 2>&1"
vim.o.shellpipe = "2>&1 | tee"
vim.o.shellquote = ""
vim.o.shellxescape = ""
vim.o.shellxquote = ""
```