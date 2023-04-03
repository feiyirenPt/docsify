---
title: vim编辑远程文件  
date: 2023-03-22 13:56  
tags:   
---

# vim编辑远程文件

> 很多时候我们需要使用远程服务器。 我们经常从这些远程服务器编辑文件。 编辑这些文件的明显解决方案之一是登录远程服务器并编辑文件。 但有时从本地计算机编辑这些文件更方便，因为我们可能已经在本地系统上安装和配置了各种插件。

Vim 支持以下协议
- SCP
- FTP
- SFTP
- HTTP (read-only)
- rsync
___

## 访问远程文件

Vim 支持使用以下语法进行远程文件编辑
```bash
vim scp://[user@]machine//absolute/path/to/file.txt
# or
vim scp://[user@]machine/relative/path/to/file.txt
```

```bash
:e dav://machine[:port]/path                      uses cadaver
:e fetch://[user@]machine/path                  uses fetch
:e ftp://[user@]machine[[:#]port]/path          uses ftp   autodetects <.netrc>
:e http://[user@]machine/path                    uses http  uses wget
:e rcp://[user@]machine/path                     uses rcp
:e rsync://[user@]machine[:port]/path         uses rsync
:e scp://[user@]machine[[:#]port]/path        uses scp
:e sftp://[user@]machine/path                    uses sftp
```

## 更改默认端口
要更改 scp,sftp 端口，有几个选项。一个快速的方法是当你打开 vim 来输入这个：

```bash
#scp
:let g:netrw_scp_cmd="scp -q -P ${port}"
#sftp
:let g:netrw_sftp_cmd="scp -q -P ${port}"
```
然后只需键入：
```bash
:e scp://my_user@remote_hostname//path/to/remote/file
```
更好的解决方案是使用 ssh 机制，即 ~/.ssh/config 文件：

```
Host lala
  HostName test.machine.example.net
  User user
  IdentityFile ~/.ssh/id_rsa
  Port 2222
```

## 使用 nread 和 nwrite

Vim 支持 nread 和 nwrite 功能，它们分别代表 net read 和 net write

```bash
:Nread scp://user@ip//tmp/message.txt
```

```bash
:Nwrite scp://jarvis@localhost//tmp/message.txt
```

## For more info
Open Vim and type the following:
```bash
:h netrw
```

## reference
- [Editing remote files via scp in vim  Vim Tips Wiki  Fandom](https://vim.fandom.com/wiki/Editing_remote_files_via_scp_in_vim)
- [vim-scripts/netrw.vim](https://github.com/vim-scripts/netrw.vim)