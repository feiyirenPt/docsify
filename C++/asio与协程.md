---
title: (4条消息) [C++] asio + C++20协程_西北丰的博客-CSDN博客_asio c++20  
date: 2023-01-11 17:36  
tags: [asio c++20]  
source: https://blog.csdn.net/jkddf9h8xd9j646x798t/article/details/128517850
---
# [[asio]]协程
## 0. 前言

自C++20为止, C++主要有以下几种风格的[[协程]]

-   回调风格
-   链式风格
-   仿线程风格, C++20协程就属于此类

其中最优雅的当属仿线程风格, 可以在一个函数中连贯地将数据流处理流程写完.

然而, C++20语言标准直接提供的标准协程是多方大佬撕逼后妥协的结果, 高度强调自由度, 并不适合直接拿来使用.

boost中有几个库实现有类似协程的功能, 比如

-   context: 提供执行栈切换的功能, 但不负责值的传递.
-   coroutine, coroutine2: 仿线程风格
-   asio: 正在适配C++20协程

本文介绍如何借助asio使用C++20协程

asio对协程的支持分两个阶段

1.  首先是将回调风格接口的简单包装成可用协程表达的awaitable对象
2.  然后是独立出executor概念
3.  最后是将io_context包装成协程context对象

当前(1.24.0)第一第二阶段的代码已经移出experimental, 可用完美适配使用了, 第三阶段的代码当前还在experimental阶段(甚至还存在编译器兼容性问题需要改源码修复).

第二阶段的代码预计C++23进入标准库std::execution, 尔后asio库在适配完标准库的executor后, 也将进入标准库std::net

## 1. awaitable

### 1.1 原始接口

首先包含头文件asio.hpp来使用下面的东西.

```cpp
#include <asio.hpp>
using namespace asio;
```

使用io_context可以创建一个没有线程池的纯调度上下文. 然后可以使用post或dispatch添加一项可执行任务.

```cpp
io_context ctx;
post(ctx, []{
    cout << "hello" << endl;
});
dispatch(ctx, []{
    cout << "world" << endl;
});
```

post是添加到任务队列尾部, dispatch是如果可以的话(如可在当前线程执行), 则立即执行.  
post和dispatch是实现异步的原始接口.

### 1.2 awaitable协程

使用co_spawn来将awaitable协程包装成任务.

```cpp
co_spawn(ctx, []() -> awaitable<void> {
    co_return;
}, detached);
```

最后在适合的线程内调用`ctx.run()`来启动协程

```cpp
ctx.run();
```

awaitable协程对外只能有返回值`co_return`, `awaitable<T>`中`T`的类型就是`co_return`的返回值的类型. 对内可以用`co_await`等待其他东西的结果.

### 1.3 co_await

以一个可await的东西timer为例

```cpp
using namespace std::chrono_literals;
io_context ctx;
steady_timer timer(ctx, 3s); // 3秒倒计时
```

在协程内使用运算符`co_await`来等待结果(timer倒计时结束)

```
co_spawn(ctx, [&]() -> awaitable<void> {
co_await timer.async_wait(use_awaitable);
cout << "hello" << endl;
}, detached);
```

### 1.4 任意和全部co_await

如果有多个可await的对象, 而只想等待其中一个, 或全部, 可使用awaitable\_operators内的运算符

```cpp
#include <asio/experimental/awaitable_operators.hpp>
using namespace std::experimental::awaitable_operators;
```

有两个timer

```cpp
steady_timer timer1(ctx, 1s);
steady_timer timer2(ctx, 2s);
```

协程内, 使用||运算符来等待任意一个完成, 用&&运算符来等待全部完成.

```cpp
co_spawn(ctx, [&]() -> awaitable<void> {
co_await (timer1.async_wait(use_awaitable) || timer2.async_wait(use_awaitable));
cout << "hello" << endl;
}, detached);
```

如果`co_await co1`得到`T`类型的值, `co_await co2`得到`U`类型的值  
那么一般情况下`co_await (co1 || co2)`得到`std::variant<T, U>`类型的值.  
`co_await (co1 && co2)`得到`std::tuple<T, U>`类型的值.

```cpp
awaitable<int> f() { co_return 123; }
awaitable<std::string> g() { co_return "hello"; }
awaitable<void> h() { co_return; }

int main() {
io_context ctx;
co_spawn(ctx, []() -> awaitable<void> {
std::tuple<int, std::string> result1 = co_await (f() && (g() && h()));
std::variant<int, std::string, std::monostate> result2 = co_await (f() || g() || h());
}, detached);
}
```

### 1.5 线程池

io_context不含执行器, 需要自行创建线程, 或直接使用主线程来启动其任务循环.  
可以使用asio提供的线程池thread_pool来取代没有线程的io_context.

```cpp
thread_pool ctx(4); // 4线程线程池
...
co_spawn(ctx, []() -> awaitable<void> {
...
}, detached);
...
ctx.join();
```

## 2. coro

### 2.1 启动

相比于只能有返回值的awaitable, coro是真正的通用协程, 不仅可以co\_return, 也可以co_yield.  
co_yield可以对外发送值, 也可以从外接收值.

```cpp
coro<std::string(double), int> co1(any_io_executor exec) {
double recv = co_yield "hello";
    std::cout << "co recv: " << recv << std::endl;
    co_return 123;
}
```

可以用coro协程启动coro协程

```cpp
coro<void> co2(any_io_executor exec) {
    auto c1 = co1(exec);
    std::string str = co_await c1(233.0);
    co_return;
}
```

也可以用awaitable协程启动coro协程, 使用async\_resume来调起coro协程

```cpp
awaitable<void> co3() {
    auto exec = co_await this_coro::executor;
    auto c1 = co1(exec);
    std::optional<std::string> res = co_await c1.async_resume(123.0,use_awaitable);
}
```

### 2.2 形参要求

coro协程一般要求形参里要有`any_io_executor`或是一个有`get_executor()`方法的对象, 如`io_context`或`tcp::socket`等.

```cpp
awaitable<void> co4(io_context& ctx) {
    co_return;
}
```

### 2.3 从this获取executor

但如果coro协程是作为方法定义的, 其中所在的类内有get\_executor方法, 那么上述形参可以放宽为自动从所在类中获取, 从而免于传入.

```cpp
struct MyCoro : public io_context {
coro<int> co5() {
    co_yield 123;
}
}
```

### 2.4 vs的编译错误修复

1.24.0版本的asio在编译时, 会出现类似"->"类型错误的提示, 原因是源码中在捕获包中使用了和类名coro相同的变量名coro, 导致编译错误  
将变量名coro改成coro以外的名字即可修复

## 3. 回调包装

### 3.1 C++式回调

将回调接口改造成协程接口是很常见的将老接口接入协程的方式.  
设有一个C++式回调接口

```cpp
template<typename Callback>
void callback(int arg, Callback func) {
    std::thread([func = std::move(func), arg]() mutable {
        std::this_thread::sleep_for(3s);
        std::move(func)(arg);
    }).detach();
}
```

如下代码可将其包装为asio式接口

```cpp
template<completion_token_for<void(int)> CompletionToken>
auto callbackWrapper(int arg, CompletionToken&& token) {
// 进行返回方式变换, 允许根据token变换返回方式, 使得可选择use_coro, use_awaitable等返回方式
    return async_initiate<CompletionToken, void(int)>([]
    (completion_handler_for<void(int)> auto handler, int arg) {
    // 放置一个空的追踪任务, 防止executor以为当前没有任务而退出
        auto work = make_work_guard(handler);
        callback(arg, [handler = std::move(handler), work = std::move(work)]
        (int result) mutable {
            dispatch(work.get_executor(), [handler = std::move(handler), result]() mutable {
            // 结束追踪任务 返回回调结果
                std::move(handler)(result);
            });
        });
    }, token, arg);
}
```

在awaitable协程中可用co_await

```cpp
int res = co_await callbackWrapper(123, use_awaitable);
```

### 3.2 C式回调

可以下载asio源码, 找到examples/cpp20/operations/c_callback_wrapper.cpp文件自行浏览, 需要补充的内容相当多, 此处暂略  
该方法要求回调式接口中能传入发起请求时的一个上下文指针, 如不能则只能使用全局变量