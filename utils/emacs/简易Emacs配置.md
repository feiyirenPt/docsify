---
title:简易Emacs配置  
date: 2023-01-15 15:55  
tags: [emacs]  
source: https://blog.csdn.net/uninterrupted/article/details/79120402
---
## 简易Emacs配置
之前看到一个笑话，大概是，某人一直跟别人说emacs怎么怎么好，自己如何如何使用emacs，后来有一天，别人看到他没有使用emacs了，问他为什么？他说，因为我一不小心把emacs的配置弄丢了，还没有备份。
其实我用着emacs觉得还挺顺手的，不想因为丢了配置文件而放弃emacs，就把我自己使用的emacs配置写成博客，放在网上，以供自己日后参考。
## Emacs版本
只用官网最新的版本。配置好window的启动项，默认使用自己的工作空间作为Emacs运行环境。
## 配置文件位置

我一般会使用到四台不同电脑办公或者学习（两台windows，一台Linux，一台双系统），所以配置文件的存放和同步是一个大问题。为了避免卡在这一步，我都使用默认的路径和配置格式。统一使用.emacs文件作为配置文件，windows的配置文件放在c盘根目录，linux的放在home目录，有更新的配置，就逐机逐文件手动更新。虽然繁琐，但是因为我的配置文件内容不多，基本上是一次性的配置工作，倒也还好。网上有很多先进的自动化更新方式，都很好，但是对于我来说，一个快速的起步更为重要。
## 配置文件内容
目前我的配置都是添加于c盘或者home目录的.emacs中
### 主题配色
在Vim上折腾够了，发现自己对于主题配色之类的不敏感，使用系统默认提供的就可以了。我使用黑色的，和Sublime保持一致。
```
(load-theme 'wombat t)
```
### 字符编码
由于操作系统的语言选项不同，我统一使用utf8，防止乱码。
```lisp
(prefer-coding-system 'utf-8)
(set-default-coding-systems 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
```
### 配置MELPA
先不管这具体内容，总之，配置好了之后，就可以一键安装软件了
```lisp
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
(package-initialize)
```
### 配置Evil
大多数人应该需要这一步，我是从VIM迁移到Emacs的，而且我十分喜欢vim的快捷键，所以就使用Evil，来在emacs中使用vim的快捷键。（VirtualStudio中可以使用Vsvim）  
更详细的内容，请参考 [emacswiki:evil]

简单来说，配置步骤如下：
1.  在配置好melpa后，输入下面的命令进行安装：
```lisp
    M-x package-refresh-contents
    M-x package-install RET evil
```
1.  安装完之后，在.emacs中加入
```lisp
    (require 'evil)
    (evil-mode 1)
```
重启Emacs之后，进入Normal模式，输入i进入插入模式。使用Ctrl+Z可以在Vim和Eamcs模式切换，注意窗口下面状态栏的的变化

### 字体

对于强迫症的我来说，我差点就因为表格中英文字体不能对齐而放弃Emacs，后来查到了cnfonts这个中文字体配置工具，相当不错。详情见GitHub：[cnfonts]。

简单的说，配置步骤如下：
1.  先配置melpa, 再输入下面的命令进行安装：
```lisp
    M-x package-install RET cnfonts RET
```
1.  在.emacs中加入
```lisp
    (require 'cnfonts)
    ;; 让 cnfonts 随着 Emacs 自动生效。
    ;; (cnfonts-enable)
    ;; 让 spacemacs mode-line 中的 Unicode 图标正确显示。
    ;; (cnfonts-set-spacemacs-fallback-fonts)
```
1.  重启Emacs，输入以下命令进行设置：
| 命令                      | 功能         |
| ------------------------- | ------------ |
| cnfonts-edit-profile      | 调整字体设置 |
| cnfonts-increase-fontsize | 增大字号     |
| cnfonts-decrease-fontsize | 减小字号     |
中文我使用文泉驿微米等宽，在文泉驿官网即可下载到，依次配置，英文，中文，对齐即可。

### org配置
其实我使用Emacs，只用org部分，写代码，我还是使用IDE，看代码，我还是使用Sublime。

-   TODO的关键字
```lisp
    (setq org-todo-keywords
          '((sequence "TODO" "|" "DONE" "CANCEL")))

    (setq org-todo-keywords
          '((sequence "TODO(t)"  "|" "DONE(d!)" "CANCEL(c!)")))
```

-   org的快捷键
```lisp
    (global-set-key "\C-cl" 'org-store-link)
    (global-set-key "\C-cc" 'org-capture)
    (global-set-key "\C-ca" 'org-agenda)
    (global-set-key "\C-cb" 'org-iswitchb)
```

-   设置自动加载org文件到安排中，以及自动加载org
```lisp
    ;; read agend data from which file
    (setq org-agenda-files (list "c:/notes_jg/org/"
                         ))
    (add-to-list 'auto-mode-alist '("\\.org\\'" . org-mode))
```

-   换行
```lisp
    (add-hook 'org-mode-hook
              (lambda()
                (setq truncate-lines nil)))
```

-   支持导出markdown
```lisp
    (eval-after-load "org"
        '(require 'ox-md nil t))
```

## 快捷键

| 按键        | 功能             |
| ----------- | ---------------- |
| S+M+RET     | 创建新条目       |
| C+c C+t     | 修改TODO的状态   |
| C+k         | 删除整行         |
| C+y         | 粘贴             |
| C+x 0       | 关闭当前窗口     |
| C+x o       | 切换窗口         |
| C+c a L     | 列出日程中的项目 |
| M+左右      | 修改TODO层级     |
| M+上下      | 移动列表         |
| C+c C+c     | 增加tag          |
| C+c C+c     | 修改checkbox     |
| C+c a m     | 搜索tag          |
| M+x         | 输入命令         |
| S+TAB       | 折叠展开         |
| S+left      | 推进状态         |
| C+c C+x C+i | 开始计时         |
| C+c C+x C+o | 停止计时         |
| C+c C+x C+s | 移动到归档文件   |
| Ctrl+z      | 使用vim模式      |

## M+x下的常用命令

<table><colgroup><col><col></colgroup><tbody><tr><td>Update time</td><td>org-evaluate-time-range</td></tr><tr><td>linum-mode</td><td>显示行号</td></tr><tr><td>goto-line</td><td>跳转到行号</td></tr></tbody></table>

[emacswiki:evil]: https://www.emacswiki.org/emacs/Evil
[cnfonts]: https://github.com/tumashu/cnfonts
