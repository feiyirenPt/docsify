---
title: packer.nvim  
date: 2022-12-21 20:43:09  
tags: neovim  
---

```lua
local fn = vim.fn
local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
end
require('packer').startup(function(use)
  -- 有意思的是，packer可以用自己管理自己。
  use 'wbthomason/packer.nvim'

  use ''
  -- your plugins here

  if packer_bootstrap then
    require('packer').sync()
  end
end)
```