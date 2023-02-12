---
title: boost中asio网络库多线程并发处理实现，以及asio在多线程模型中线程的调度情况和线程安全。 
date: 2023-02-11 01:14  
tags: [asio,C++]  
source: https://www.cnblogs.com/lidabo/p/3906055.html  
---
1、实现多线程方法：

其实就是多个线程同时调用`io_service::run`

```cpp
        for (int i = 0; i != m_nThreads; ++i)  
        {  
            boost::shared_ptr<boost::thread> pTh(new boost::thread(  
                boost::bind(&boost::asio::io_service::run,&m_ioService)));  
            m_listThread.push_back(pTh);  
        }

```
2、多线程调度情况：

asio规定：只能在调用`io_service::run`的线程中才能调用事件完成处理器。

注：事件完成处理器就是你`async_accept、async_write`等注册的句柄，类似于回调的东西。

单线程：

如果只有一个线程调用`io_service::run`，根据asio的规定，事件完成处理器也只能在这个线程中执行。也就是说，你所有代码都在同一个线程中运行，因此变量的访问是安全的。

多线程：

如果有多个线程同时调用`io_service::run`以实现多线程并发处理。对于asio来说，这些线程都是平等的，没有主次之分。如果你投递的一个请求比如`async_write`完成时，asio将随机的激活调用io_service::run的线程。并在这个线程中调用事件完成处理器（`async_write`当时注册的句柄）。如果你的代码耗时较长，这个时候你投递的另一个async_write请求完成时，asio将不等待你的代码处理完成，它将在另外的一个调用`io_service::run`线程中，调用`async_write`当时注册的句柄。也就是说，你注册的事件完成处理器有可能同时在多个线程中调用。

当然你可以使用 `boost::asio::io_service::strand`让完成事件处理器的调用，在同一时间只有一个， 比如下面的的代码：

```cpp
  socket_.async_read_some(boost::asio::buffer(buffer_),  
      strand_.wrap(  
        boost::bind(&connection::handle_read, shared_from_this(),  
          boost::asio::placeholders::error,  
          boost::asio::placeholders::bytes_transferred)));

...

boost::asio::io_service::strand strand_;
```

此时async_read_som完成后掉用handle_read时，必须等待其它handle_read调用完成时才能被执行（async_read_som引起的handle_read调用）。

多线程调用时，还有一个重要的问题，那就是无序化。比如说，你短时间内投递多个async_write，那么完成处理器的调用并不是按照你投递async_write的顺序调用的。asio第一次调用完成事件处理器，有可能是第二次async_write返回的结果，也有可能是第3次的。使用strand也是这样的。strand只是保证同一时间只运行一个完成处理器，但它并不保证顺序。

代码测试：

服务器：

将下面的代码编译以后，使用cmd命令提示符下传人参数<IP> <port> <threads>调用

比如：`test.exe 0.0.0.0 3005 10   `

客服端 使用windows自带的telnet

cmd命令提示符：

```bash
telnet 127.0.0.1 3005
```

原理：客户端连接成功后，同一时间调用100次boost::asio::async_write给客户端发送数据，并且在完成事件处理器中打印调用序号，和线程ID。

核心代码：

```cpp
    void start()  
    {  
        for (int i = 0; i != 100; ++i)  
        {  
            boost::shared_ptr<string> pStr(new string);  
            *pStr = boost::lexical_cast<string>(boost::this_thread::get_id());  
            *pStr += "rn";  
            boost::asio::async_write(m_nSocket,boost::asio::buffer(*pStr),  
                boost::bind(&CMyTcpConnection::HandleWrite,shared_from_this(),  
                 boost::asio::placeholders::error,  
                 boost::asio::placeholders::bytes_transferred,  
                 pStr,i)  
                );  
        }  
    }

//去掉 boost::mutex::scoped_lock lk(m_ioMutex); 效果更明显。

    void HandleWrite(const boost::system::error_code& error  
        ,std::size_t bytes_transferred  
        ,boost::shared_ptr<string> pStr,int nIndex)  
    {  
        if (!error)  
        {  
            boost::mutex::scoped_lock lk(m_ioMutex);  
            cout << "发送序号=" << nIndex << ",线程id=" << boost::this_thread::get_id() << endl;  
        }  
        else  
        {  
            cout << "连接断开" << endl;  
        }  
    }

```
完整代码：

```cpp
#include <boost/bind.hpp>  
#include <boost/shared_ptr.hpp>  
#include <boost/enable_shared_from_this.hpp>  
#include <boost/asio.hpp>  
#include <boost/lexical_cast.hpp>  
#include <boost/thread.hpp>  
#include <boost/thread/mutex.hpp>  
#include <string>  
#include <iostream>

using std::cout;  
using std::endl;  
using std::string;  
using boost::asio::ip::tcp;

class CMyTcpConnection  
    : public boost::enable_shared_from_this<CMyTcpConnection>  
{  
public:  
    CMyTcpConnection(boost::asio::io_service &ser)  
        :m_nSocket(ser)  
    {  
    }  
    typedef boost::shared_ptr<CMyTcpConnection> CPMyTcpCon;

    static CPMyTcpCon CreateNew(boost::asio::io_service& io_service)  
    {  
        return CPMyTcpCon(new CMyTcpConnection(io_service));  
    }

   public:  
    void start()  
    {  
        for (int i = 0; i != 100; ++i)  
        {  
            boost::shared_ptr<string> pStr(new string);  
            *pStr = boost::lexical_cast<string>(boost::this_thread::get_id());  
            *pStr += "rn";  
            boost::asio::async_write(m_nSocket,boost::asio::buffer(*pStr),  
                boost::bind(&CMyTcpConnection::HandleWrite,shared_from_this(),  
                 boost::asio::placeholders::error,  
                 boost::asio::placeholders::bytes_transferred,  
                 pStr,i)  
                );  
        }  
    }  
    tcp::socket& socket()  
    {  
        return m_nSocket;  
    }  
private:  
    void HandleWrite(const boost::system::error_code& error  
        ,std::size_t bytes_transferred  
        ,boost::shared_ptr<string> pStr,int nIndex)  
    {  
        if (!error)  
        {  
            boost::mutex::scoped_lock lk(m_ioMutex);  
            cout << "发送序号=" << nIndex << ",线程id=" << boost::this_thread::get_id() << endl;  
        }  
        else  
        {  
            cout << "连接断开" << endl;  
        }  
    }  
private:  
    tcp::socket m_nSocket;  
    boost::mutex m_ioMutex;  
};

class CMyService  
    : private boost::noncopyable  
{  
public:  
    CMyService(string const &strIP,string const &strPort,int nThreads)  
        :m_tcpAcceptor(m_ioService)  
        ,m_nThreads(nThreads)  
    {  
        tcp::resolver resolver(m_ioService);  
        tcp::resolver::query query(strIP,strPort);  
        tcp::resolver::iterator endpoint_iterator = resolver.resolve(query);  
        boost::asio::ip::tcp::endpoint endpoint = *resolver.resolve(query);  
        m_tcpAcceptor.open(endpoint.protocol());  
        m_tcpAcceptor.set_option(boost::asio::ip::tcp::acceptor::reuse_address(true));  
        m_tcpAcceptor.bind(endpoint);  
        m_tcpAcceptor.listen();

        StartAccept();  
    }  
    ~CMyService(){Stop();}  
public:  
    void Stop()   
    {   
        m_ioService.stop();  
        for (std::vector<boost::shared_ptr<boost::thread>>::const_iterator it = m_listThread.cbegin();  
            it != m_listThread.cend(); ++ it)  
        {  
            (*it)->join();  
        }  
    }  
    void Start()  
    {  
        for (int i = 0; i != m_nThreads; ++i)  
        {  
            boost::shared_ptr<boost::thread> pTh(new boost::thread(  
                boost::bind(&boost::asio::io_service::run,&m_ioService)));  
            m_listThread.push_back(pTh);  
        }  
    }  
private:  
    void HandleAccept(const boost::system::error_code& error  
        ,boost::shared_ptr<CMyTcpConnection> newConnect)  
    {  
        if (!error)  
        {  
            newConnect->start();  
        }  
        StartAccept();  
    }

    void StartAccept()  
    {  
        CMyTcpConnection::CPMyTcpCon newConnect = CMyTcpConnection::CreateNew(m_tcpAcceptor.get_io_service());  
        m_tcpAcceptor.async_accept(newConnect->socket(),  
            boost::bind(&CMyService::HandleAccept, this,  
            boost::asio::placeholders::error,newConnect));  
    }  
private:  
    boost::asio::io_service m_ioService;  
    boost::asio::ip::tcp::acceptor m_tcpAcceptor;  
    std::vector<boost::shared_ptr<boost::thread>> m_listThread;  
    std::size_t m_nThreads;  
};

int main(int argc, char* argv[])  
{  
    try  
    {  
        if (argc != 4)  
        {  
            std::cerr << "<IP> <port> <threads>n";  
            return 1;  
        }  
        int nThreads = boost::lexical_cast<int>(argv[3]);  
        CMyService mySer(argv[1],argv[2],nThreads);  
        mySer.Start();  
        getchar();  
        mySer.Stop();  
    }  
    catch (std::exception& e)  
    {  
        std::cerr << "Exception: " << e.what() << "n";  
    }  
    return 0;  
}
```

测试发现和上面的理论是一致的，发送序号是乱的，线程ID也不是同一个。

asio多线程中线程的合理个数：

作为服务器，在不考虑省电的情况下，应该尽可能的使用cpu。也就是说，为了让cpu都忙起来，你的线程个数应该大于等于你电脑的cpu核心数（一个核心运行一个线程）。具体的值没有最优方案，大多数人使用cpu核心数*2 + 2的这种方案，但它不一定适合你的情况。

asio在windows xp等系统中的实现：

asio在windows下使用完成端口，如果你投递的请求没有完成，那么这些线程都在等待GetQueuedCompletionStatus的返回，也就是等待内核对象，此时线程是不占用cpu时间的。
