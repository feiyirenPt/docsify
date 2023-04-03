---
title: weak_ptr的使用场景
date: 2023-02-23 23:52  
tags: [weak_ptr,C++]  
source: https://blog.csdn.net/zhizhengguan/article/details/123808609  
---
## 第一种：观察者功能

> 理解

-   **std::weak_ptr是解决悬空指针问题的一种很好的方法**。仅通过使用原始指针，就不可能知道使用的数据是否已经被释放。相反，通过std::shared_ptr管理数据并将std::weak_ptr提供给数据用户，用户可以通过expired()或者lock()来检测数据的有效性
-   您不能单独使用std::shared_ptr来执行此操作，因为所有std::shared_ptr实例共享数据的所有权，而在删除std::shared_ptr的所有实例之前，这些所有权不会被删除。

> 理解

-   shared_ptr：保存实际对象
-   weak_ptr：使用lock连接到真实所有者，否则返回NULL

大致来说，[weak_ptr]角色类似于房屋中介的角色。没有中介，要出租房屋，我们可能必须检查城市中的随机房屋。代理商可以确保我们仅拜访哪些仍然可以访问而且可以供出租的房屋

![在这里插入图片描述][fig1]

> 理解

我们知道std::[shared_ptr]会共享对象的所有权，但是有一些场景如果有一个像std::shared_ptr但是又不参与资源所有权共享的指针是很方便的。换句话说，是一个类似std::shared_ptr但不影响对象引用计数的指针。不参与资源所有权就意味着不会对资源的生命周期产生影响，有利于对象之间的解耦。

举个一个不太恰当的例子，A和B相互加了微信，假设我们用一个指针来指向自己的微信朋友，如果是shared_ptr，那么A和B的生命周期是相互影响的，而实际上我们并不希望这种强绑定，比如假设B注销了账户，A根本不用知道，只有当A想发消息给B的时候系统才会发出提示：您还不是该用户的朋友。这时候weak_ptr就派上用场了。这也就是weak_ptr的第一种使用场景：

**当你想使用对象，但是并不想管理对象，并且在需要使用对象时可以判断对象是否还存在**

这种模式就是观察者模式：

-   观察者模式是在subject状态发生改变时，通知观察者的一种设计模式。
-   在多数实现中，每个subject持有指向观察者的指针，这使得当subject状态改变时可以很容易通知观察者。
-   subject不会控制其观察者的生存期，因此应该是持有观察者的weak_ptr指针。同时在subject的使用某个指针时，可以先确定是否空悬。比如当某个微信用户需要群发消息给所有的好友（这里假设观察者是微信好像），实际上假如对方已经删除了好友这条消息是发布出去，weak_ptr相对于是提供了一个种方法来判断对方是否已经删好友了的功能，如果没删就发消息；删了就不理会。

> 方法

weak_ptr内几个重要成员函数：

-   成员函数use_count() 观测资源引用计数
-   成员函数expired() 功能相当于 use_count()==0 表示被观测的资源(也就是shared_ptr的管理的资源)是否被销毁
-   成员函数lock()从被观测的shared_ptr获得一个可用的shared_ptr对象， 进而操作资源。但当expired()==true的时候，lock()函数将返回一个存储空指针的shared_ptr

```
class CTxxx {
public:    
CTxxx() {printf( "CTxxx cstn" );}
~CTxxx() {printf( "CTxxx dstn" );    
};
    
int main() {
    std::shared_ptr<CTxxx> sp_ct(new CTxxx);
    std::weak_ptr<CTxxx> wk_ct = sp_ct;
    std::weak_ptr<CTxxx> wka1;
    {
        std::cout << "wk_ct.expired()=" << wk_ct.expired() << std::endl;
        std::shared_ptr<CTxxx> tmpP = wk_ct.lock();
        if (tmpP) {
            std::cout << "tmpP usecount=" << tmpP.use_count() << std::endl;
        } else {
            std::cout << "tmpP invalid" << std::endl;
        }
        std::shared_ptr<CTxxx> a1(new CTxxx);
        wka1 = (a1);
    }
    std::cout << "wka1.expired()=" << wka1.expired() << std::endl;
    std::cout << "wka1.lock()=" << wka1.lock() << std::endl;
 
    std::shared_ptr<CTxxx> cpySp = wka1.lock();
    if (cpySp) std::cout << "cpySp is ok" << std::endl;
    else std::cout << "cpySp is destroyed" << std::endl;
    return 1;
}

```

## 第二种：解决循环引用

![在这里插入图片描述][fig2]

A、B、C三个对象的数据结构中，A和C共享B的所有权，因此各持有一个指向B的std::shared_ptr;

假设有一个指针从B指回A（即上图中的红色箭头），则该指针的类型应为weak_ptr，而不能是裸指针或shared_ptr，原因如下：

-   假如是裸指针，当A被析构时，由于C仍指向B，所以B会被保留。但B中保存着指向A的空悬指针（野指针），而B却检测不出来，但解引用该指针时会产生未定义行为。
-   假如是shared_ptr时。由于A和B相互保存着指向对方的shared_ptr，此时会形成循环引用，从而阻止了A和B的析构。
-   假如是weak_ptr，这可以避免循环引用。假设A被析构，那么B的回指指针会空悬，但B可以检测到这一点，同时由于该指针是weak_ptr，不会影响A的强引用计数，因此当shared_ptr不再指向A时，不会阻止A的析构。

还是以微信好友为例，删好友是不用对方同意，如果用shared_ptr就意味着我删不了你，你也删不了我。示例代码如下：

```
class B; // 前置声明类B
class A
{
public:
A() { cout << "A()" << endl; }
~A() { cout << "~A()" << endl; }
weak_ptr<B> _ptrb; // 指向B对象的弱智能指针。引用对象时，用弱智能指针
};
class B
{
public:
B() { cout << "B()" << endl; }
~B() { cout << "~B()" << endl; }
weak_ptr<A> _ptra; // 指向A对象的弱智能指针。引用对象时，用弱智能指针
};
int main()
{
    // 定义对象时，用强智能指针
shared_ptr<A> ptra(new A());// ptra指向A对象，A的引用计数为1
shared_ptr<B> ptrb(new B());// ptrb指向B对象，B的引用计数为1

    // A对象的成员变量_ptrb也指向B对象，B的引用计数为1，因为是弱智能指针，引用计数没有改变
ptra->_ptrb = ptrb;
// B对象的成员变量_ptra也指向A对象，A的引用计数为1，因为是弱智能指针，引用计数没有改变
ptrb->_ptra = ptra;

cout << ptra.use_count() << endl; // 打印结果:1
cout << ptrb.use_count() << endl; // 打印结果:1

/*
出main函数作用域，ptra和ptrb两个局部对象析构，分别给A对象和
B对象的引用计数从1减到0，达到释放A和B的条件，因此new出来的A和B对象

```

怎么办？只需要将A或B的任意一个成员变量改为weak_ptr：

```
#include <iostream>
#include <memory>
using namespace std;
class A {
public:
std::weak_ptr<B> bptr; // 修改为weak_ptr
~A() {
cout << "A is deleted" << endl;
}
};
class B {
public:
std::shared_ptr<A> aptr;
~B() {
cout << "B is deleted" << endl;
}
};
int main()
{
{//设定一个作用域
std::shared_ptr<A> ap(new A);
std::shared_ptr<B> bp(new B);
ap->bptr = bp;
bp->aptr = ap;
}
cout<< "main leave" << endl; 
return 0;
}

```

## 第三种：缓存对象

-   考虑一个工厂函数loadWidget，该函数基于唯一ID来创建一些指向只读对象的智能指针。
-   假设该只读对象需要被频繁使用，而且经常需要从文件或数据库中加载。那么可以考虑将对象缓存起来。同时为了避免过量缓存，当不再使用时，则将该对象删除。
-   由于带缓存，工厂函数返回unique_ptr类型显然不合适。因为调用者和缓存管理器均需要一个指向这些对象的指针。
-   当用户用完工厂函数返回的对象后，该对象会被析构，此时相应的缓存条目将会空悬。因为可以考虑将工厂函数的返回值设定为shared_ptr类型，而缓存类型为weak_ptr类型。

## 第四种：线程安全的对象回调与析构 —— 弱回调

有时候我们需要“如果对象还活着，就调用它的成员函数，否则忽略之”的语意，就像Observable::notifyObservers()那样，我称之为“弱回调”。这也是可以实现的，利用weak_ptr，我们可以把weak_ptr绑到boost::function里，这样对象的生命期就不会被延长。然后在回调的时候先尝试提升为shared_ptr，如果提升成功，说明接受回调的对象还健在，那么就执行回调；如果提升失败，就不必劳神了。

muduo的源代码，该源码中对于智能指针的应用非常优秀，其中借助shared_ptr和weak_ptr解决了这样一个问题，多线程访问共享对象的线程安全问题，解释如下：线程A和线程B访问一个共享的对象，如果线程A正在析构这个对象的时候，线程B又要调用该共享对象的成员方法，此时可能线程A已经把对象析构完了，线程B再去访问该对象，就会发生不可预期的错误。

```
class Test
{
public:
// 构造Test对象，_ptr指向一块int堆内存，初始值是20
Test() :_ptr(new int(20)) 
{
cout << "Test()" << endl;
}
// 析构Test对象，释放_ptr指向的堆内存
~Test()
{
delete _ptr;
_ptr = nullptr;
cout << "~Test()" << endl;
}
// 该show会在另外一个线程中被执行
void show()
{
cout << *_ptr << endl;
}
private:
int *volatile _ptr;
};
void threadProc(weak_ptr<Test> pw) // 通过弱智能指针观察强智能指针
{
// 睡眠两秒
std::this_thread::sleep_for(std::chrono::seconds(2));
/* 
如果想访问对象的方法，先通过pw的lock方法进行提升操作，把weak_ptr提升
为shared_ptr强智能指针，提升过程中，是通过检测它所观察的强智能指针保存
的Test对象的引用计数，来判定Test对象是否存活，ps如果为nullptr，说明Test对象
已经析构，不能再访问；如果ps!=nullptr，则可以正常访问Test对象的方法。
*/
shared_ptr<Test> ps = pw.lock();
if (ps != nullptr)
{
ps->show();
}
}
int main()
{
// 在堆上定义共享对象
shared_ptr<Test> p(new Test);
// 使用C++11的线程，开启一个新线程，并传入共享对象的弱智能指针
std::thread t1(threadProc, weak_ptr<Test>(p));
// 在main线程中析构Test共享对象
// 等待子线程运行结束
t1.join();
return 0;
}

```

运行上面的代码，show方法可以打印出20，因为main线程调用了t1.join()方法等待子线程结束，此时pw通过lock提升为ps成功，见上面代码示例。

如果设置t1为分离线程，让main主线程结束，p智能指针析构，进而把Test对象析构，此时show方法已经不会被调用，因为在threadProc方法中，pw提升到ps时，lock方法判定Test对象已经析构，提升失败！main函数代码可以如下修改测试：

```
int main()
{
// 在堆上定义共享对象
shared_ptr<Test> p(new Test);
// 使用C++11的线程，开启一个新线程，并传入共享对象的弱智能指针
std::thread t1(threadProc, weak_ptr<Test>(p));
// 在main线程中析构Test共享对象
// 设置子线程分离
t1.detach();
return 0;
}

```

该main函数运行后，最终的threadProc中，show方法不会被执行到。以上是在多线程中访问共享对象时，对shared_ptr和weak_ptr的一个典型应用。

[fig1]: https://img-blog.csdnimg.cn/1f3362f8410a40f7b2696bff270bdc8e.png
[fig2]: https://img-blog.csdnimg.cn/583726c18d114a8aafaa2bff06b96fe5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAT2NlYW5TdGFy55qE5a2m5Lmg56yU6K6w,size_14,color_FFFFFF,t_70,g_se,x_16
[fig3]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png
[fig4]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png

[weak_ptr]: https://so.csdn.net/so/search?q=weak_ptr&spm=1001.2101.3001.7020
[shared_ptr]: https://so.csdn.net/so/search?q=shared_ptr&spm=1001.2101.3001.7020
