---
title: 我的 Neovim 配置框架：one.nvim - 知乎  
date: 2023-01-19 23:12  
tags: [NeoVim]  
source: https://zhuanlan.zhihu.com/p/583324604
---
分享一个我用 Lua 编写的 Neovim 一体化配置框架。早用 lua 早日摆脱 vimscript。

## 特性

-   用 Lua 管理 nvim 配置。所有配置项都可覆盖。
-   充分使用 Neovim 功能：Native LSP、Float Window、Winbar。
-   基于 [vim-plug] 或 [packer.nvim] 的插件框架，任你选择。
-   帅气的界面和配色。暗黑模式。支持真彩色、平滑滚动、滚动条、Dashboard。你可以修改配色，详见 [doc/colors.md]。
-   支持配置 github 代理，在中国大陆可加快插件下载速度。
-   集成了 120 多个 Vim/Nvim 插件。增强插件的使用体验，并且修复了一些插件的缺点。

## 插件列表

-   插件管理器: [vim-plug] (默认) 或 [packer]
-   面板: [alpha.nvim]
-   大纲: [aerial] (默认) 或 [majutsushi/tagbar]
-   文件浏览器: [neo-tree] (默认) 或 [nerdtree] 或 [nvim-tree]
-   状态栏: [lualine] (默认) 或 [airline]
-   Tab 栏: [tabby]
-   Buffer 栏: [barbar] 或 [bufferline] (如果使用 Buffer 栏，你要禁用 Tab 栏插件)
-   光标栏高亮: [beacon] (默认) 或 [specs.nvim]
-   滚动条: [nvim-scrollbar]
-   平滑滚动: [neoscroll.nvim]
-   会话: [persisted] (默认) 或 [possession] 或 [xolox/vim-session] 或 [rmagatti/auto-session]
-   模糊查找: [telescope] 与 [ctrlsf]
-   Diagnostics 窗口: [trouble]
-   撤销: [vim-mundo]
-   语法高亮: [treesitter] 与 [nvim-ts-rainbow] 与 [nvim-treesitter-pairs]
-   单词高亮: [vim-interestingwords]
-   注释代码: [Comment.nvim] (默认) 或 [nerdcommenter]
-   LSP: [nvim-lspconfig] 与 [treesitter] 与 [null-ls] 与 [nlsp] 与 [goto-preview] 与 [lsp-toggle]
-   DAP: [nvim-dap]
-   格式化: [lsp-format] 与 [editorconfig-vim]
-   Formatter, Linter, LSP, DAP 管理器: [mason] 与 [mason-installer]
-   补全: [nvim-cmp]
-   Snippets: [nvim-snippy]
-   Markdown: [plasticboy/vim-markdown] 与 [markdown-preview] 与 [headlines.nvim] 与 [vim-MarkdownTOC]
-   括号配对: [nvim-surround] 与 [nvim-autopairs] 与 [nvim-ts-autotag] 与 [vim-matchup]
-   Git: [gitsigns] 与 [lazygit] 与 [diffview.nvim]
-   缩进基准线: [indent-blankline]
-   光标移动: [hop.nvim] 与 [accelerated-jk]
-   窗口选择: [nvim-window-picker] (默认) 或 [yorickpeterse/nvim-window] 或 [vim-choosewin]
-   窗口大小调整: [simeji/winresizer] 与 [windows.nvim]
-   Context: [aerial] (默认) 或 [navic] 与 [nvim-treesitter-context]
-   文本对齐: [vim-easy-align]
-   书签: [vim-bookmarks]
-   标记: [marks.nvim]
-   日历: [mattn/calendar-vim]
-   Curl: [rest.nvim]
-   Icons: [devicons] 与 [icon-picker]
-   UI 增强: [dressing] 和 [noice]
-   启动加速: [impatient.nvim]
-   跳出输入模式的快捷键: [better-escape.nvim]
-   Increment: [increment-activator]
-   Filetype: [filetype.nvim]
-   Latex: [nabla]
-   通知: [notify] (默认) 或 [notifier]
-   性能调优: [vim-startuptime]
-   Text-Objects: [wildfire] 与 [nvim-treesitter-textobjects]
-   表格: [vim-table-mode]
-   终端: [neoterm]
-   测试: [nvim-test]
-   TODO 注释: [todo-comments]
-   尾空格: [whitespace]
-   复制粘贴: [yanky]
-   禅模式: [twilight 与 zen-mode]
-   笔记本: [zk]
-   实时命令: [live-command]
-   颜色着色: [nvim-colorizer]
-   [游戏]

## 截图

![][fig1]

Dashboard

![][fig2]

主界面

![][fig3]

提纲

![][fig4]

Finder

![][fig5]

快捷键

![][fig6]

Diagnostic

![][fig7]

代码补全

![][fig8]

函数签名补全

## 依赖

-   [NVIM v0.8] 及以上版本
-   python3、pip3
-   nvim python provider
-   `pip3 install --upgrade --user pynvim`
-   `pip2 install --upgrade --user pynvim` (这是可选的)
-   Git 与 curl
-   C 编译器与 libstdc++。([treesitter] 需要)
-   [Nerd Font 字体]。推荐 [DejaVuSansMonoForPowerline Nerd Font]。记得修改你的终端的字体设置。
-   [ripgrep(rg)]
-   支持 Linux 和 MacOS，不支持 Windows

## 安装

你可使用 git clone 安装本项目。或在容器中运行 nvim。

### git clone

```
PACK_DIR=${XDG_DATA_HOME:-$HOME/.local/share}/nvim/site/pack/user/start
mkdir -p "$PACK_DIR"
git clone --depth 1 --single-branch https://github.com/adoyle-h/one.nvim.git "$PACK_DIR"/one.nvim

# Set your nvim config directory
NVIM_HOME=${XDG_CONFIG_HOME:-$HOME/.config}/nvim
mkdir -p "$NVIM_HOME"
echo "require('one').setup {}" > "$NVIM_HOME"/init.lua
```

[初始化]后，执行 `nvim` 启动。

### 容器

你可以在容器里运行它。这要求你的主机已安装 docker。

### 构建容器

执行 `./scripts/build-container`。 （建议中国地区用户加上 `-p` 参数使用代理，加快构建速度）。

**苹果芯片的 Mac 用户注意**。当前 nvim 未提供 Arm 架构下的发行版。所以容器构建和运行都使用了 `--platform=linux/amd64` 选项。苹果芯片下运行容器会很卡。

### 使用容器

```
# 在主机上缓存 nvim 数据
docker volume create nvim-data
# 建议把这行 alias 加到 ~/.bashrc
alias nvim='docker run --rm -it --platform linux/amd64 -v "$HOME/.config/nvim:/root/.config/nvim" -v "nvim-data:/root/.local/share/nvim" -v "$PWD:/workspace" adoyle/one.nvim:v0.8.0'
```

[初始化]后，执行 `nvim` 启动。

## 配置

所有配置项都是可选的。

### 用户配置

你可以传入自定义配置来覆盖默认配置。

```
require('one').setup {
  config = {
    colors = { -- basic colors
      white = '#BEC0C4', -- frontground
      black = '#15181D', -- background
      cursorLine = '#252931',
    },

    ['mason-installer'] = {
      ensureInstalled = {
        'lua-language-server',
        'luaformatter',
        'bash-language-server',
      }
    }
  },

  -- Add your plugins or override plugin default options.
  -- More examples in ./lua/one/plugins.lua
  plugins = {
    -- { 'profiling', disable = false },
    -- { 'psliwka/vim-smoothie', disable = false },
  },
}
```

你可参考[我的 init.lua] 来编写你的配置。

你可以覆盖插件的默认选项。详见 [插件 - 使用插件]。

### 默认配置

### configFn(config)

有些插件配置需要用到对应的模块。例如 `null-ls` 的 `sources` 配置项。你必须定义在 `configFn(config)` 函数。 函数的返回值必须是一个 table，它会被合并到 `config` 变量。

```
require('one').setup {
  configFn = function(config)
    local builtins = require('null-ls').builtins
    local codeActions = builtins.code_actions
    local diagnostics = builtins.diagnostics
    local formatting = builtins.formatting

    -- Do not return config, only return the overridden parts
    return {
      nullLS = {
        sources = {
          codeActions.eslint_d,
          codeActions.shellcheck,
          diagnostics.eslint_d,
          formatting.eslint_d.with {
            prefer_local = 'node_modules/.bin',
          },
          formatting.lua_format,
        },
      },
    }
  end,
}
```

### 覆盖插件参数

通过 `require('one').setup {plugins = {}}`，你可以覆盖任何[插件参数]。你可以覆盖配色和快捷键设置。

### 查看配置

你可以通过编写 lua 脚本访问 `require('one.config').config` 或 `a.CM.config` 获取配置信息.

同时，这里提供了两个命令来查看配置： `:ShowConfig` 查看最终合并的配置。 `:ShowPlugins` 查看加载的和未加载的插件。

## 插件管理器

选择你喜欢的插件管理器，目前提供 `vim-plug` (默认) 和 `packer`。

```
require('one').setup {
  config = {
    pluginManager = { use = 'packer' }, -- 'vim-plug' or 'packer'
  },
}
```

vim-plug 管理的插件目录和 packer 管理的是不一样的。当你改变了 `config.pluginManager.use` 的值，需要重装插件。详见[初始化]流程。

-   Packer [默认配置]
-   Vim-Plug [默认配置]

## 插件

所有插件都可以被关闭，覆盖默认配置项，或者替换成你喜欢的插件。自定义配置和扩展非常方便。

插件的定义和使用，详见[./doc/plugin.md]。

你甚至可以设置 `onlyPlugins = {}` 来一键禁用所有插件（不禁用插件管理器）。详见 [Debug - Disable other plugins]。

## 代理

```
require('one').setup {
  config = {
    proxy = {
      -- 如果你在中国大陆，推荐使用 'https://ghproxy.com'。否则，不要设置该配置项。
      github = 'https://ghproxy.com',
    },
  },
}
```

有些插件使用了 git submodule，代理无法起作用。建议你执行 `git config --global http.https://github.com.proxy https://ghproxy.com` 设置全局代理。

## 使用

### LSP

本项目使用 [nvim-lspconfig] 和 [null-ls] 来配置 LSP，管理 LSP 与 Nvim 的连接。 使用 [mason.nvim] 来安装与管理 lsp，dap 和 null-ls 的第三方包。

### 格代化码式

本项目基于 LSP 来格式化代码。 使用 `lsp-format` 代替 nvim 内置的 `vim.lsp.buf.format`，提供更灵活的自定义配置。详见 [lsp-format 选项]。

### Telescope 插件

本项目实现了很多有用的 Telescope 插件，详见 [ad-telescope-extensions.nvim] 和 [./lua/one/plugins/telescope/extensions.lua]。

可使用 `<space>;` 快捷键查询所有 Telescope 插件。

### 窗口选择器

![][fig9]

按下 `<C-w><C-w>` 打开选择器浏览所有 Tab 和窗口。 按下 `<CR>` 跳转到对应的窗口或者 Tab。

### 浮动命令栏

该功能默认未开启，因为还不稳定。 你可以依照下面的代码启用。

```
require('one').setup {
  plugins = {
    { 'noice', disable = false },
  },
}
```

它会隐藏命令栏。当 `:`, `/`, `?` 按下会弹出窗口。

![][fig10]

## 扩展你自己的插件、高亮、命令等配置

```
local my = {}

my.highlights = function(config)
  local c = config.colors
  return { CmpGhostText = { fg = c.grey4, bg = c.darkBlue } }
end

my.commands = {
  Hello = ':echo world'
}

require('one').setup {
  plugins = { my },
}
```

## 全局变量

你可以在运行时操作 one.nvim 的属性。

```
    ╭─────────────────────╮
    │   one.CM        CMD │
    │   one.FT        CMD │
    │   one.PM        CMD │
    │   one.cmp       CMD │
    │   one.util      CMD │
    │   one.setup     CMD │
    │   one.consts    CMD │
    │   one.telescope CMD │
    ╰─────────────────────╯
:lua one.
```

它默认分配到全局变量 `one`。（看配置项 `config.global = 'one'`） 可以改成其他变量名，随你喜欢。或者设置 `false` 或 `nil`，不创建该全局变量。

这很酷，不是吗？

## 其他项目

我创建的[其他 nvim 项目]。

___

以上就简单介绍 one.nvim 这个项目（其实就是删减了 README 文档后复制粘贴过来的 ，省略了很多功能细节）。项目文档写得很详细，中英双语。觉得好就点个 star 吧。

[fig1]: https://pic2.zhimg.com/v2-75d51fc1c812b03e5f17bd60115ba6bd_b.jpg
[fig2]: https://pic4.zhimg.com/v2-3ab05e42947ca9117aa8d386c7c73823_b.jpg
[fig3]: https://pic2.zhimg.com/v2-5ff63bc7b6a32b05fd2d951468c848cd_b.jpg
[fig4]: https://pic2.zhimg.com/v2-706ce9f4f62db4dcff2e1a9348475eb5_b.jpg
[fig5]: https://pic2.zhimg.com/v2-d207d99b0ca88e828d3f7fd53d4957a1_b.jpg
[fig6]: https://pic2.zhimg.com/v2-4d301c6f61694b6c5650ef67b8175265_b.jpg
[fig7]: https://pic1.zhimg.com/v2-ce880a3bb02815eda1a60a9e52480c98_b.jpg
[fig8]: https://pic4.zhimg.com/v2-b8f7617f62b62b422b8f4270094fb5f3_b.jpg
[fig9]: https://pic4.zhimg.com/v2-1e360e1d996f4998a29a8ae4cb01dda3_b.jpg
[fig10]: https://pic4.zhimg.com/v2-3be40632c274fdf0e155cfa8dbbee967_b.jpg

[vim-plug]: https://link.zhihu.com/?target=https%3A//github.com/junegunn/vim-plug
[packer.nvim]: https://link.zhihu.com/?target=https%3A//github.com/wbthomason/packer.nvim
[doc/colors.md]: https://zhuanlan.zhihu.com/p/583324604/doc/colors.md
[vim-plug]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugin-manager/vim-plug.lua
[packer]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugin-manager/packer.lua
[alpha.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/alpha.lua
[aerial]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/aerial.lua
[majutsushi/tagbar]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/tagbar.lua
[neo-tree]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/neo-tree.lua
[nerdtree]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/nerdtree.lua
[nvim-tree]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/nvim-tree.lua
[lualine]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lualine.lua
[airline]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/airline.lua
[tabby]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/tabby.lua
[barbar]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/barbar.lua
[bufferline]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/bufferline.lua
[beacon]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/beacon.lua
[specs.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/specs.lua
[nvim-scrollbar]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/scrollbar.lua
[neoscroll.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/scroll.lua
[persisted]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/session/persisted.lua
[possession]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/session/possession.lua
[xolox/vim-session]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/session/vim-session.lua
[rmagatti/auto-session]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/session/auto-session.lua
[telescope]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/telescope/main.lua
[ctrlsf]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/search/ctrlsf.lua
[trouble]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/trouble.lua
[vim-mundo]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/undotree.lua
[treesitter]: https://link.zhihu.com/?target=https%3A//github.com/nvim-treesitter/nvim-treesitter
[nvim-ts-rainbow]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/treesitter/rainbow.lua
[nvim-treesitter-pairs]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/treesitter/pairs.lua
[vim-interestingwords]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/highlight-words.lua
[Comment.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/comment.lua
[nerdcommenter]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/comment_nerd.lua
[nvim-lspconfig]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lsp/main.lua
[treesitter]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/treesitter/init.lua
[null-ls]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lsp/null-ls.lua
[nlsp]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lsp/nlsp.lua
[goto-preview]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lsp/preview.lua
[lsp-toggle]: https://link.zhihu.com/?target=https%3A//github.com/adoyle-h/lsp-toggle.nvim
[nvim-dap]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/dap/init.lua
[lsp-format]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lsp/format.lua
[editorconfig-vim]: https://link.zhihu.com/?target=https%3A//github.com/editorconfig/editorconfig-vim
[mason]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lsp/mason.lua
[mason-installer]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/lsp/mason-installer.lua
[nvim-cmp]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/completion/init.lua
[nvim-snippy]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/completion/snippet.lua
[plasticboy/vim-markdown]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/markdown/main.lua
[markdown-preview]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/markdown/preview.lua
[headlines.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/markdown/headlines.lua
[vim-MarkdownTOC]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/markdown/toc.lua
[nvim-surround]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/match/surround.lua
[nvim-autopairs]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/match/autopairs.lua
[nvim-ts-autotag]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/match/ts-autotag.lua
[vim-matchup]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/match/matchup.lua
[gitsigns]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/git/sign.lua
[lazygit]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/git/lazygit.lua
[diffview.nvim]: https://link.zhihu.com/?target=https%3A//github.com/sindrets/diffview.nvim
[indent-blankline]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/indent-line.lua
[hop.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/move/jump.lua
[accelerated-jk]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/move/accelerated.lua
[nvim-window-picker]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/move/window-picker.lua
[yorickpeterse/nvim-window]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/move/window-selector.lua
[vim-choosewin]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/move/choose-window.lua
[simeji/winresizer]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/window/resize.lua
[windows.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/window/maximize.lua
[aerial]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/aerial.lua
[navic]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/navic.lua
[nvim-treesitter-context]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/treesitter/context.lua
[vim-easy-align]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/align.lua
[vim-bookmarks]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/bookmark.lua
[marks.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/mark.lua
[mattn/calendar-vim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/calendar.lua
[rest.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/curl.lua
[devicons]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/devicons.lua
[icon-picker]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/icon-picker.lua
[dressing]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/dressing.lua
[noice]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/noice.lua
[impatient.nvim]: https://link.zhihu.com/?target=https%3A//github.com/lewis6991/impatient.nvim
[better-escape.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/escape.lua
[increment-activator]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/increment.lua
[filetype.nvim]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/filetype.lua
[nabla]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/latex.lua
[notify]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/notify.lua
[notifier]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/notifier.lua
[vim-startuptime]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/profiling.lua
[wildfire]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/select.lua
[nvim-treesitter-textobjects]: https://link.zhihu.com/?target=https%3A//github.com/nvim-treesitter/nvim-treesitter-textobjects
[vim-table-mode]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/table.lua
[neoterm]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/terminal/neoterm.lua
[nvim-test]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/test.lua
[todo-comments]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/todo.lua
[whitespace]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/trailing.lua
[yanky]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/yank.lua
[twilight 与 zen-mode]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/zen.lua
[zk]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/zk.lua
[live-command]: https://link.zhihu.com/?target=https%3A//github.com/smjonas/live-command.nvim
[nvim-colorizer]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/colors/inline.lua
[游戏]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/funny.lua
[NVIM v0.8]: https://link.zhihu.com/?target=https%3A//github.com/neovim/neovim/releases/tag/v0.8.0
[treesitter]: https://link.zhihu.com/?target=https%3A//github.com/nvim-treesitter/nvim-treesitter%23requirements
[Nerd Font 字体]: https://link.zhihu.com/?target=https%3A//github.com/ryanoasis/nerd-fonts
[DejaVuSansMonoForPowerline Nerd Font]: https://link.zhihu.com/?target=https%3A//github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/DejaVuSansMono
[ripgrep(rg)]: https://link.zhihu.com/?target=https%3A//github.com/BurntSushi/ripgrep
[初始化]: https://zhuanlan.zhihu.com/p/583324604/edit#%E5%88%9D%E5%A7%8B%E5%8C%96
[初始化]: https://zhuanlan.zhihu.com/p/583324604/edit#%E5%88%9D%E5%A7%8B%E5%8C%96
[我的 init.lua]: https://link.zhihu.com/?target=https%3A//github.com/adoyle-h/neovim-config/blob/master/init.lua
[插件 - 使用插件]: https://zhuanlan.zhihu.com/p/583324604/doc/plugin.zh.md#%E4%BD%BF%E7%94%A8%E6%8F%92%E4%BB%B6
[插件参数]: https://zhuanlan.zhihu.com/p/583324604/doc/plugin.zh.md#%E6%8F%92%E4%BB%B6%E5%8F%82%E6%95%B0
[初始化]: https://zhuanlan.zhihu.com/p/583324604/edit#%E5%88%9D%E5%A7%8B%E5%8C%96
[默认配置]: https://zhuanlan.zhihu.com/p/583324604/lua/one/config/packer.lua
[默认配置]: https://zhuanlan.zhihu.com/p/583324604/lua/one/config/vim-plug.lua
[./doc/plugin.md]: https://zhuanlan.zhihu.com/p/583324604/doc/plugin.md
[Debug - Disable other plugins]: https://zhuanlan.zhihu.com/p/583324604/doc/debug.md#disable-other-plugins
[nvim-lspconfig]: https://link.zhihu.com/?target=https%3A//github.com/neovim/nvim-lspconfig
[null-ls]: https://link.zhihu.com/?target=https%3A//github.com/jose-elias-alvarez/null-ls.nvim
[mason.nvim]: https://link.zhihu.com/?target=https%3A//github.com/williamboman/mason.nvim
[lsp-format 选项]: https://link.zhihu.com/?target=https%3A//github.com/lukas-reineke/lsp-format.nvim%23special-format-options
[ad-telescope-extensions.nvim]: https://link.zhihu.com/?target=https%3A//github.com/adoyle-h/ad-telescope-extensions.nvim
[./lua/one/plugins/telescope/extensions.lua]: https://zhuanlan.zhihu.com/p/583324604/lua/one/plugins/telescope/extensions.lua
[其他 nvim 项目]: https://link.zhihu.com/?target=https%3A//github.com/adoyle-h%3Ftab%3Drepositories%26q%3D%26type%3Dsource%26language%3Dlua%26sort%3Dstargazers
