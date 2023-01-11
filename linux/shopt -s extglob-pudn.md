---
title: shell opt extglob  
date: 2023-01-11 17:19  
tags: [linux]  
source: https://www.pudn.com/news/630c891a88df2007aaeeecdd.html
---

-   [linux]
-   [php]
-   [运维]

## 1、简介

> shopt，即shell option，用于显示和设置shell中的行为选项，通过这些选项以增强shell易用性。

## 2、用法

```bash
shopt [-sup] [optionName]
```

其中：

-   -s：打开某个选项
-   -u：关闭某个选项
-   -p：列出所有可设置的选项

shopt查看所有选项及其值
```bash

[root@localhost~ ] shopt
autocd         off
cdable_vars    off
cdspell        off
checkhash      off
checkjobs      off
checkwinsize   on
cmdhist        on
compat31       off
compat32       off
compat40       off
dirspell       off
dotglob        off
execfail       off
expand_aliases on
extdebug       off
extglob        on
extquote       on
failglob       off
force_fignore  on
globstar       off
gnu_errfmt     off
histappend     off
histreedit     off
histverify     off
hostcomplete   on
huponexit      off
interactive_commentson
lithist        off
login_shell    on
mailwarn       off
no_empty_cmd_completionoff
nocaseglob     off
nocasematch    off
nullglob       off
progcomp       on
promptvars     on
restricted_shelloff
shift_verbose  off
sourcepath     on
xpg_echo       off
[root@master four]# shopt
autocd         off
cdable_vars    off
cdspell        off
checkhash      off
checkjobs      off
checkwinsize   on
cmdhist        on
compat31       off
compat32       off
compat40       off
dirspell       off
dotglob        off
execfail       off
expand_aliases on
extdebug       off
extglob        on
extquote       on
failglob       off
force_fignore  on
globstar       off
gnu_errfmt     off
histappend     off
histreedit     off
histverify     off
hostcomplete   on
huponexit      off
interactive_commentson
lithist        off
login_shell    on
mailwarn       off
no_empty_cmd_completionoff
nocaseglob     off
nocasematch    off
nullglob       off
progcomp       on
promptvars     on
restricted_shelloff
shift_verbose  off
sourcepath     on
xpg_echo       off
```

## 3、常用参数extglob—开启扩展模式匹配

> shopt的选项很多，常用的有extglob，用于开启扩展模式匹配。开启之后Shell可以另外识别出5个模式匹配操作符，能使文件匹配更加方便。

```bash
- 查看extglob选项的状态
shopt extglob

- 开启extglob
shopt -s extglob

- 关闭extglob
shopt -u extglob
```

开启extglob，Shell可以另外识别出5个模式匹配操作符：

| 匹配操作符       | 含义                         |
| ---------------- | ---------------------------- |
| ?(pattern-list)  | 所给模式匹配0次或1次         |
| \*(pattern-list) | 所给模式匹配0次以上，包括0次 |
| +(pattern-list)  | 所给模式匹配1次以上，包括1次 |
| @(pattern-list)  | 所给模式仅仅匹配一次         |
| ！(pattern-list) | 不匹配括号内的所给模式       |

**实例一：删除文件名不以sh结尾的文件**

```bash
rm -rf !(*sh)
```

当然换种思路也能实现：

```bash
ls | grep -v  *.sh | xargs rm -rf
```

**实例二：删除文件名以txt、php、tar结尾的文件**

```bash
rm -rf *@(txt|php|tar)
```
## 使用shopt设置set ±o特性

>可以使用shopt设置或者取消那些由set ±o控制的特性。使用常规的shopt –s或者-u语法，并包含-o选项。举例来说，下面的命令将开启noclobber特性：
```bash
shopt –o –s noclobber
```

[linux]: https://www.pudn.com/search?q=linux
[php]: https://www.pudn.com/search?q=php
[运维]: https://www.pudn.com/search?q=%E8%BF%90%E7%BB%B4