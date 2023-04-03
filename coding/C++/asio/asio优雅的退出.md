---
title: asio优雅的退出  
date: 2023-02-25 16:42  
tags: [asio,C++]  
source: https://blog.csdn.net/ycf8788/article/details/54604336    
---

# asio优雅的退出

> boost::asio算是一个比较成熟的网络库，不过在某些方面在异步上的接口实现却不是很友好，感觉官方的很多文档描述的都太简单了，甚是忧伤。

回归正题，最近一直在研究asio的关闭流程，发现相关的信息确实不多。简单总结了下大致就是先关闭 socket再关闭io_service。但是内部有很多细节的问题没有考虑到。

- 总结的一些注意点
    1. 一定要确保io_service相关的资源都要先释放掉，例如socket。因为如果ios_service调用stop后，如果 socket再进行相关的操作，可能会导致stop失效。

    2. 通过调用async_connect接口进行异步连接时，调用socket.close或者 socket.cancel，并不会立即失败，因为是异步的操作。

    3. io_service.stop调用后，不可以立马释放io_service对象，否则就有可能会报ERROR_ABANDONED_WAIT_0的异常。

- socket的释放建议:
    1. 如果已经建立链接，则最好要优先调用shutdown接口，然后调用cancel和close。
    2. 如果正在连接或者未连接，调用cancel和close即可。

- io_service的关闭建议：
    1. 优先关闭其他相关的资源
    2. 调用stop接口
    3. 需要等待工作者线程退出，再释放io_service对象。（目前没有找到合适的方式知道工作者线程何时退出完毕）


### 关于asio ssl退出
- [参考](https://www.codenong.com/32046034/)