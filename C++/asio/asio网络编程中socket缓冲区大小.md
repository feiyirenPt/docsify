---
title: asio网络编程中socket缓冲区大小  
date: 2023-02-16 16:39  
tags:   
---

# asio网络编程中socket缓冲区大小

## 问题

socket传送稍微大点的二进制文件就抛出` 系统检测到在一个调用中尝试使用指针参数时的无效指针地址`的异常


## 解决方案

[查阅资料][MSDN]得知win下socket缓冲器大小为65536字节(滑动窗口大小),最大可自动扩容到4倍的65536字节

asio设置socket buffer_size

```cpp
asio::socket_base::send_buffer_size size_option(65536);
tcpSocket.set_option(size_option);
asio::socket_base::receive_buffer_size size_option(nSize);
tcpsocket.set_option(size_option);
```


[MSDN]: https://learn.microsoft.com/zh-cn/troubleshoot/windows-server/networking/description-tcp-features#tcp-window-size
