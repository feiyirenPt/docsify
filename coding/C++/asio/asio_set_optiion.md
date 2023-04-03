---
title: boost asio set_option用法  
date: 2023-03-03 10:41  
tags: [asio set_option]  
source: https://blog.csdn.net/qq_33053671/article/details/106477850  
---

## 基本用法

-   get_io_service()：这个函数返回构造函数中传入的io_service实例
-   get_option(option)：这个函数返回一个套接字的属性
-   set_option(option)：这个函数设置一个套接字的属性
-   io_control(cmd)：这个函数在套接字上执行一个I/O指令

![在这里插入图片描述][fig2]

## 使用方法

```cpp
#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>
#include <boost/thread.hpp>

using namespace boost;


int main(int argc, const char * argv[]) 
{
boost::asio::io_service service;
boost::asio::ip::tcp::endpoint ep( boost::asio::ip::address::from_string("127.0.0.1"), 80);
boost::asio::ip::tcp::socket sock(service);
//sock.connect(ep);
sock.open(boost::asio::ip::tcp::v4());   //不open就直接set_option会有问题
// TCP套接字可以重用地址
boost::asio::ip::tcp::socket::reuse_address ra(true);
boost::system::error_code err_code;
sock.set_option(ra);    // 复用
sock.set_option(boost::asio::ip::tcp::no_delay(true), err_code);  //设置为数据立即发送，避免延迟；有副作用，导致网络传输效率降低
sock.set_option(boost::asio::socket_base::linger(true, 0), err_code); //设置socket关闭时，立即关闭
sock.set_option(boost::asio::socket_base::keep_alive(true));

boost::asio::ip::tcp::socket::receive_buffer_size rbs;
sock.get_option(rbs);
return 0;

}
```

## 参考网址

[Boost.Asio 网络编程（[译]Boost.Asio基本原理）]  
[Boost.Asio C++ 网络编程]

[fig2]: https://img-blog.csdnimg.cn/20200601172413477.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMDUzNjcx,size_16,color_FFFFFF,t_70

[Boost.Asio 网络编程（[译]Boost.Asio基本原理）]: https://www.cnblogs.com/fnlingnzb-learner/p/10408812.html
[Boost.Asio C++ 网络编程]: https://mmoaay.gitbooks.io/boost-asio-cpp-network-programming-chinese/content/Chapter2.html
