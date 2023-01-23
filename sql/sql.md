---
title: sql  
date: 2022-10-9  
tags: sql  
---
## win下中文问题

设置mysql默认字符集utf-8
代码中设置终端 system("chcp 65001")
mingw gcc g++ 默认UTF-8无问题
cmake-msvc 默认 utf-BOM (UNICODE)
除非cmake设置  

add_compile_options("$<$<C_COMPILER_ID:MSVC>:/utf-8>")  
add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/utf-8>

[参考链接](https://www.coder.work/article/6860828)

但mysql不认得utf-8 with BOM ,解决办法

1. 统一UTF-8
2. 文件UTF-8 with BOM ,代码中string = u8"string" (C++11)
   [参考链接](https://www.cnblogs.com/Esfog/p/MSVC_UTF8_CHARSET_HANDLE.html)

## null值无法读取

先mysql_fetch_row判断null

## mysql cmake c 需要

* libcrypto-1_1-x64.dll  
* libmysql.dll
* libmysql.lib
* libssl-11-x64.dll

