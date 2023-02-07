---
title: toggleterm设置powershell  
date: 2023-1-15 23:52:09  
tags: neovim  
---
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