---
title: asio错误码  
date: 2023-02-25 16:45  
tags: [asop,C++]  
source:  http://www.cppblog.com/shanoa/archive/2011/05/06/145840.html  
---

# asio错误码

boost::asio网络传输错误码的一些实验结果（recv error_code）
错误码很重要，可以由此判断网络连接到底发生了神马事情，从而驱动高层逻辑的行为。只有笼统的错误码判断的网络层是不够规范的，鄙人觉得有些错误码还是需要在网络层就区分开的，特此记录一些当前实验的错误码以及发生原因。

以下是一部分在async_receive()的handler处捕获到的比较有用的错误码

| 错误码（十进制） | 枚举                                  | 发现原因                                                                                                                                    |
| ---------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 10009            | boost::asio::error::bad_descriptor    | 在一个已经关闭了的套接字上执行async_receive()                                                                                               |
| 995              | boost::asio::error::operation_aborted | 正在async_receive()异步任务等待时，本端关闭套接字                                                                                           |
| 10054            | boost::asio::error::connection_reset  | 正在async_receive()异步任务等待时，远端的TCP协议层发送RESET终止链接，暴力关闭套接字。常常发生于远端进程强制关闭时，操作系统释放套接字资源。 |
| 2                | boost::asio::error::eof               | 正在async_receive()异步任务等待时，远端关闭套接字                                                                                           |

## reference
- [所有错误码](https://en.cppreference.com/w/cpp/error/errc)