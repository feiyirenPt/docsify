---
title: io_context run 直接返回了  
date: 2023-02-10 17:42  
tags: [asio]]  
source: https://blog.csdn.net/fengge8ylf/article/details/6796175  
---

 当有任务的时候，run函数会一直阻塞；但当没有任务了，run函数会返回，所有异步操作终止。

在一个客户端程序中，如果我想连接断开后重连，由于连接断开了，run会返回，当再次重连的时候，由于run返回了，即使连接成功了，也不会调用`aysnc_connect`绑定的回调函数。

有两个解决方法。

1.再次重连的时候，要重新调用run函数，在调用的前一定要调用`io_context::reset`.
以便`io_context::run`重用。
```cpp

```

2. 用`boost::asio::io_context::work`

```cpp
    boost::asio::io_context io_context_;
    boost::asio::io_context::work work(io_context_);
    io_context_.run();
```