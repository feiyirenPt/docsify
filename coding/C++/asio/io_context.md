---
title: io_context工作原理  
date: 2023-02-09 23:47  
tags: [io_context]  
source: 
- https://blog.csdn.net/qq_41172631/article/details/106819462  
- https://blog.csdn.net/fengge8ylf/article/details/6796175  
---

[Boost].Asio可用于对I / O对象（例如套接字）执行同步和异步操作。

## I/O模型

io_context对象是asio框架中的调度器，所有异步io事件都是通过它来分发处理的（io对象的构造函数中都需要传入一个io_service对象）。在同步事件中会使用一个默认的

```cpp
asio::io_context io_context;
asio::ip::tcp::socket socket(io_context)
```

### 同步IO主要执行流程

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020061722140181.png)

1.  您的程序将至少有一个io_context对象。 io_context表示程序到操作系统的I / O服务的链接。

> boost::asio::io_context io_context;

2.  要执行I / O操作，您的程序将需要一个I / O对象，例如TCP套接字

```cpp
boost::asio::ip::tcp::socket socket(io_context);
```

##### 当执行同步连接操作时，将发生以下事件序列

1.  您的程序通过调用I / O对象来启动连接操作

```cpp
socket.connect(server_endpoint);
```

2.  I / O对象将请求转发到io_context。
3.  io上下文调用操作系统来执行连接操作。
4.  操作系统将操作的结果返回给io上下文。
5.  io_context将由操作导致的任何错误转换为boost :: system :: error_code类型的对象,传给IO对象
6.  如果操作失败，则I / O对象将引发类型boost :: system :: system_error的异常。

```cpp
boost::system::error_code ec;  
socket.connect(server_endpoint, ec);
```

### 异步IO主要执行流程

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200617221843793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTcyNjMx,size_16,color_FFFFFF,t_70)

1.  您的程序通过调用I / O对象来启动连接操作

> socket.async_connect(server_endpoint, your_completion_handler);

其中 your_completion_handler为一个回调函数

1.  I/O对象将请求转发到io_context。
2.  io上下文向操作系统发出应该启动异步连接的信号  
    ![在这里插入图片描述][fig2]
3.  操作系统通过将结果放在一个队列上来指示连接操作已经完成，等待io上下文拾取。
4.  您的程序必须调用io context::run()(或一个类似的io context成员函数)，以便检索结果。当有未完成的异步操作时，对io context::run()的调用会阻塞，所以通常会在开始第一个异步操作时调用它。
5.  在对io上下文::run()的调用中，io上下文将操作的结果取出队列，将其转换为错误代码，然后将其传递给完成处理程序（回调函数）

## 保活

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


[fig2]: https://img-blog.csdnimg.cn/2020061722253167.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTcyNjMx,size_16,color_FFFFFF,t_70
