---
title: wsl与win剪贴板互通  
date: 2023-1-15 23:49:09  
tags: neovim  
---

```lua
if vim.fn.has('wsl') == 1 then
	vim.cmd [[
	let g:clipboard = {
		  \   'name': 'myClipboard',
		  \   'copy': {
		  \      '+': ['/mnt/c/windows/system32/clip.exe'],
		  \      '*': ['/mnt/c/windows/system32/clip.exe'],
		  \    },
		  \   'paste': {
		  \      '+': ['/mnt/c/windows/system32/clip.exe'],
		  \      '*': ['/mnt/c/windows/system32/clip.exe'],
		  \   },
		  \   'cache_enabled': 1,
		  \ }
]]
else
	vim.o.clipboard = "" --unnamed unnamedplus
end
```