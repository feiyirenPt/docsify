---
title: (6条消息) C++11：再谈shared_ptr，以及shared_ptr参数传递以及构造细节_zzhongcy的博客-CSDN博客_shared_ptr 参数  
date: 2023-02-08 00:20  
tags: [shared_ptr 参数]  
source: https://blog.csdn.net/zzhongcy/article/details/90476959
---
**本文根据众多互联网博客内容整理后形成，引用内容的版权归原始作者所有，仅限于学习研究使用**

     shared_ptr在boost库中已经有多年了，C++11又为其正名，把他引入了STL库，放到了std的下面，可见其颇有用武之地；但是shared_ptr是万能的吗？有没有什么样的问题呢？本文并不说明shared_ptr的设计原理，也不是为了说明如何使用，只说一下在使用过程中的几点注意事项。

## 参数值传递

代码如下：

```cpp
#include <iostream>  
#include <boost/shared_ptr.hpp>  
#include <boost/make_shared.hpp>

void funcx(**boost::shared_ptr<int> c**, int b) {  
    std::cout << "after: "   
        << "&c " << static_cast<void *>(&c) << ", "  
        << "c.get() " << static_cast<void *>(c.get()) << ", "  
        << "&b " << static_cast<void *>(&b) << std::endl;  
}  
int main(int argc, char *argv) {  
    int a = 2;  
    int b = 3;  
    **boost::shared_ptr<int> c = boost::make_shared<int>(a);**  
    std::cout << "first: "   
            << "&c " << static_cast<void *>(&c) << ", "   
            << "c.get() " << static_cast<void *>(c.get()) << ", "  
            << "&b " << static_cast<void *>(&b) << ", "  
            << "&a " << static_cast<void *>(&a) << std::endl;  
    funcx(c, b);  
    system("pause");  
    return 1;  
}
```
输出结果如下： **智能指针值传递：智能指针已经是个拷贝，但是指向的值还是一个地址。**

```
first:  &c **003FF988**, c.get() **004B0A04**, &b 003FF998, &a 003FF9A4  
after: &c **003FF444**, c.get() **004B0A04**, &b 003FF44C
```

## **传值还是传引用？**

C/C++的函数参数传递有两种方式：传值(pass-by-value)和传引用(pass-by-reference).

```cpp
void pass_by_value(t t);  
void pass_by_value(t0);  
void pass_by_reference(const t& t);  
void pass_by_reference2(t& t);  
```

      传值方式会带来一次额外的对象拷贝构造函数调用开销，在pass_by_value中，编译器会调用T的拷贝构造函数从t0构造出一个新的临时的T对象用作pass_by_value的参数，这个对象在函数pass_by_value函数调用结束后会自动析构。

     而传引用方式不存在这次额外的构造函数调用，可以简单的理解为传了一个地址作为pass_by_reference的参数。

     当构造一个T对象开销很大时，显然，传引用方式具有明显的性能优势。

     对于shared_ptr对象，究竟哪种方式更好呢？

```cpp
// case 1: pass by value  
void pass_shared_ptr(boost::shared_ptr<t> t);

// case 2: pass by reference  
void pass_shared_ptr(const boost::shared_ptr<t>& t){  
   ...  
   t->dosomething();  
}
```

      两种情况的区别正如上述，第一种情况多了一次额外的shared_ptr对象拷贝构造函数的调用。 乍一看，还是传引用的好，但事实并非如此。

       使用shared_ptr对象隐含一个假设，就是在shared_ptr对象的作用范围中，它一定指向一个存在并有效的内存对象，也就是说它的引用计数一定为1。**在传引用的情况下，如果...代码中对shared_ptr对象有副作用时，比如传入的t是一个对象的成员变量而这个对象又正好被释放了，那么这个shared_ptr的引用计数可能被减为0从而导致所指对象的释放**，然后悲剧就发生了，t->doSomething(), 企图在t上解引用去调用一个方法将会导致segment falut。

       但这毕竟是一个由于code不小心而引入的意外，如果你能确保...代码块中没有对t的副作用，传引用也不会存在大问题。然而，防范于未然应当是每个程序员的编程习惯。

      再说说传值，额外多出的一次对象拷贝正是保证了在shared_ptr对象的作用域中它一定能指向一个有效的内存对象这一假设，而shared_ptr对象的拷贝算不算上是重量级的。这个优化实际上没有多大意义。

### 所以，传递shared_ptr参数还是用传值更好！

## 智能指针是万能良药？

      智能指针为解决资源泄漏，编写异常安全代码提供了一种解决方案，那么他是万能的良药吗？使用智能指针，就不会再有资源泄漏了吗？来看下面的代码：

```cpp
//header file  
void func( shared_ptr<T1> ptr1, shared ptr<T2> ptr2 );

  //call func like this  
func( shared_ptr<T1>( new T1() ), shared_ptr<T2>( new T2() ) );
```

      上面的函数调用，看起来是安全的，但在现实世界中，其实不然：由于C++并未定义一个表达式的求值顺序，因此上述函数调用除了func在最后得到调用之外是可以确定，其他的执行序列则很可能被拆分成如下步骤：

-   a.    分配内存给T1
-   b.   构造T1对象
-   c.    分配内存给T2
-   d.   构造T2对象
-   e.    构造T1的智能指针对象
-   f.     构造T2的智能指针对象
-   g.   调用func

或者：

-   a’. 分配内存给T1
-   b’. 分配内存给T2
-   c’. 构造T1对象
-   d’. 构造T2对象
-   e’. 构造T1的智能指针对象
-   f’. 构造T2的智能指针对象
-   g’. 调用func

    **上述无论哪种形式的构造序列，如果在c或者d / c’或者d’失败，则T1对象所分配内存必然泄漏**。

    为解决这个问题，有一个依然使用智能智能的笨重办法：

```cpp
template<class T>_ptr<T> shared_ptr_new(){
    return shared_ptr<T>( new T );
}//call like this( shared_ptr_new<T1>(), shared_ptr_new<T2>() );
```

      使用这种方法，可以解决因为产生异常导致资源泄漏的问题；然而另外一个问题出现了，如果T1或者T2的构造函数需要提供参数怎么办呢？难道提供很多个重载版本？——可以倒是可以，只要你不嫌累，而且有足够的先见性。  
      其实，最最完美的方案，其实是最简单的——就是尽量简单的书写代码，像这样：

**智能指针值传递：**

```cpp
//header fileunc( shared_ptr<T1> ptr1, shared_ptr<T2> ptr2 );
//call func like this_ptr<T1> ptr1( new T1() );_ptr<T2> ptr2( new T2() );(ptr1, ptr2  );
```

      这样简简单单的代码，避免了异常导致的泄漏。又应了那句话：简单就是美。其实，在一个表达式中，分配多个资源，或者需要求多个值等操作都是不安全的。

归总一句话：抛弃临时对象，让所有的智能指针都有名字，就可以避免此类问题的发生。

## shared_ptr 交叉引用导致的泄漏

      是否让每个智能指针都有了名字，就不会再有内存泄漏？不一定。看看下面代码的输出，是否感到惊讶？

```cpp
class CLeader;
class CMember;
 
class CLeader
{
public:
      CLeader() { cout << "CLeader::CLeader()" << endl; }
      ~CLeader() { cout << "CLeader:;~CLeader() " << endl; }
 
      std::shared_ptr<CMember> member;
};
 
class CMember
{
public:
      CMember()  { cout << "CMember::CMember()" << endl; }
      ~CMember() { cout << "CMember::~CMember() " << endl; }
 
      std::shared_ptr<CLeader> leader;   
};
 
void TestSharedPtrCrossReference()
{
      cout << "TestCrossReference<<<" << endl;
      boost::shared_ptr<CLeader> ptrleader( new CLeader );
      boost::shared_ptr<CMember> ptrmember( new CMember );
 
      ptrleader->member = ptrmember;
      ptrmember->leader = ptrleader;
 
      cout <<"  ptrleader.use_count: " << ptrleader.use_count() << endl;
      cout <<"  ptrmember.use_count: " << ptrmember.use_count() << endl;
}
```

  
```
//output:  
CLeader::CLeader()  
CMember::CMember()  
  ptrleader.use_count: 2  
  ptrmember.use_count: 2  
```
      从运行输出来看，两个对象的析构函数都没有调用，也就是出现了内存泄漏——原因在于：TestSharedPtrCrossReference（）函数退出时，**两个shared_ptr对象的引用计数都是2，所以不会释放对象**；

![][fig2]

      这里出现了常见的交叉引用问题，这个问题，即使用原生指针互相记录时也需要格外小心；shared_ptr在这里也跌了跟头，ptrleader和ptrmember在离开作用域的时候，由于引用计数不为1，所以最后一次的release操作（shared_ptr析构函数里面调用）也无法destroy掉所托管的资源。

      为了解决这种问题，可以采用weak_ptr来隔断交叉引用中的回路。所谓的weak_ptr，是一种弱引用，表示只是对某个对象的一个引用和使用，而不做管理工作；我们把他和shared_ptr来做一下对比：

![][fig3]

     由于weak_ptr具有上述的一些性质，所以如果把CMember的声明改成如下形式，就可以解除这种循环，从而每个资源都可以顺利释放。

```cpp
class CMember  
{  
public:  
      CMember()  { cout << "CMember::CMember()" << endl; }  
      ~CMember() { cout << "CMember::~CMember() " << endl; }

        boost::weak_ptr<CLeader> leader;     
};  
```
      这种使用weak_ptr的方式，是基于已暴露问题的修正方案，在做设计的时候，一般很难注意到这一点；

     总之，C++缺少垃圾收集机制，虽然智能指针提供了一个的解决方案，但他也难以到达完美；因此，C++中的资源管理必须慎之又慎。

## 类向外传递this与shared_ptr

      可以说，shared_ptr着力解决类对象一级的资源管理，至于类对象内部，shared_ptr暂时还无法管理；那么这是否会出现问题呢？来看看这样的代码：

```cpp
class Point1  
{  
public:  
    Point1() :  X(0), Y(0) { cout << "Point1::Point1(), (" << X << "," << Y << ")" << endl; }  
    Point1(int x, int y) :  X(x), Y(y) { cout << "Point1::Point1(int x, int y), (" << X << "," << Y << ")" << endl; }  
    ~Point1() { cout << "Point1::~Point1(), (" << X << "," << Y << ")" << endl; }  
public:  
    **Point1*** Add(const Point1* rhs) { X += rhs->X; Y += rhs->Y; **return this;**}  
private:  
    int X;  
    int Y;  
};

  void TestPoint1Add()  
{  
    cout << "TestPoint1Add() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;  
    **shared_ptr<Point1> p1( new Point1(2,2) );  
    shared_ptr<Point1> p2( new Point1(3,3) );**

          **p2.reset( p1->Add(p2.get()) );**
}
```

```
  输出为：  
TestPoint1Add() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
Point1::Point1(int x, int y), (2,2)  
Point1::Point1(int x, int y), (3,3)  
Point1::~Point1(), (3,3)  
Point1::~Point1(), (5,5)  
**Point1::~Point1(), (5411568,5243076)**  
```
      为了使类似Point::Add()::Add()可以连续进行Add操作成为可能，P**oint1定义了Add方法，并返回了this指针（从Effective C++的条款看，这里最好该以传值形式返回临时变量，在此为了说明问题，暂且不考虑这种设计是否合理，但他就这样存在了）**。在TestPoint1Add（）函数中，使用此返回的指针重置了p2，这样p2和p1就同时管理了同一个对象，但是他们却互相不知道这事儿，于是悲剧发生了。**在作用域结束的时候，他们两个都去对所管理的资源进行析构**，从而出现了上述的输出。从最后一行输出也可以看出，所管理的资源，已经处于“无效”的状态了。

那么，我们是否可以改变一下呢，让Add返回一个shared_ptr了呢。我们来看看Point2:

```cpp
class Point2  
{  
public:  
    Point2() :  X(0), Y(0) { cout << "Point2::Point2(), (" << X << "," << Y << ")" << endl; }  
    Point2(int x, int y) :  X(x), Y(y) { cout << "Point2::Point2(int x, int y), (" << X << "," << Y << ")" << endl; }  
    ~Point2() { cout << "Point2::~Point2(), (" << X << "," << Y << ")" << endl; }  
public:  
    shared_ptr<Point2> Add(const Point2* rhs) { X += rhs->X; Y += rhs->Y; return shared_ptr<Point2>(this);}  
private:  
    int X;  
    int Y;  
};

  void TestPoint2Add()  
{  
    cout << endl << "TestPoint2Add() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;  
    **shared_ptr<Point2> p1( new Point2(2,2) );  
    shared_ptr<Point2> p2( new Point2(3,3) );**

          **p2.swap( p1->Add(p2.get()) );**
}
```

```
  输出为：  
TestPoint2Add() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
Point2::Point2(int x, int y), (2,2)  
Point2::Point2(int x, int y), (3,3)  
Point2::~Point2(), (3,3)  
Point2::~Point2(), (5,5)  
**Point2::~Point2(), (3379952,3211460)**
```

      从输出来看，哪怕使用shared_ptr来作为Add函数的返回值，仍然无济于事；**对象仍然被删除了两次**；

      针对这种情况，shared_ptr的解决方案是： **enable_shared_from_this这个模版类**。所有需要在内部传递this指针的类，都从enable_shared_from_this继承；在需要传递this的时候，使用其成员函数shared_from_this()来返回一个shared_ptr。运用这种方案，我们改良我们的Point类，得到如下的Point3：

```cpp
class Point3 : **public enable_shared_from_this<Point3>**  
{  
public:  
    Point3() :  X(0), Y(0) { cout << "Point3::Point3(), (" << X << "," << Y << ")" << endl; }  
    Point3(int x, int y) :  X(x), Y(y) { cout << "Point3::Point3(int x, int y), (" << X << "," << Y << ")" << endl; }  
    ~Point3() { cout << "Point3::~Point3(), (" << X << "," << Y << ")" << endl; }

      public:  
    **shared_ptr<Point3>** Add(const Point3* rhs) { X += rhs->X; Y += rhs->Y; **return shared_from_this();**}

  private:  
    int X;  
    int Y;  
};

  void TestPoint3Add()  
{  
    cout << endl << "TestPoint3Add() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" << endl;  
    shared_ptr<Point3> p1( new Point3(2,2) );  
    shared_ptr<Point3> p2( new Point3(3,3) );

          p2.swap( p1->Add(p2.get()) );  
}  
```
```
输出为：  
TestPoint3Add() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
Point3::Point3(int x, int y), (2,2)  
Point3::Point3(int x, int y), (3,3)  
Point3::~Point3(), (3,3)  
Point3::~Point3(), (5,5)  
```
      从这个输出可以看出，在这里的对象析构已经变得正常。因此，**在类内部需要传递this的场景下，enable_shared_from_this是一个比较靠谱的方案；只不过，要谨慎的记住，使用该方案的一个前提，就是类的对象已经被shared_ptr管理，否则，就等着抛异常吧**。例如：

Point3 p1(10, 10);  
Point3 p2(20, 20);

  p1.Add( &p2 ); //此处抛异常

      上面的代码会导致crash。那是因为p1没有被shared_ptr管理。之所以这样，是由于shared_ptr的构造函数才会去初始化enable_shared_from_this相关的引用计数（具体可以参考代码），所以如果对象没有被shared_ptr管理，shared_from_this()函数就会出错。  
于是，shared_ptr又引入了注意事项：

1.  若要在内部传递this，请考虑从enable_shared_from_this继承
2.  若从enable_shared_from_this继承，则类对象必须让shared_ptr接管。
3.  如果要使用智能指针，那么就要保持一致，统统使用智能智能，尽量减少raw pointer裸指针的使用。

1.  C++没有垃圾收集，资源管理需要自己来做。
2.  智能指针可以部分解决资源管理的工作，但是不是万能的。
3.  使用智能指针的时候，每个shared_ptr对象都应该有一个名字；也就是避免在一个表达式内做多个资源的初始化；
4.  避免shared_ptr的交叉引用；使用weak_ptr打破交叉；
5.  **使用enable_shared_from_this机制来把this从类内部传递出来；**
6.  资源管理保持统一风格，要么使用智能指针，要么就全部自己管理裸指针；

转自：

[https://blog.csdn.net/henan_lujun/article/details/8984543]

[https://blog.csdn.net/muyuxuebao/article/details/51253204]

[fig1]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png
[fig2]: https://img-blog.csdnimg.cn/20190523112904542.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhbmd5YW5neWU=,size_16,color_FFFFFF,t_70
[fig3]: https://img-blog.csdnimg.cn/20190523113141298.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhbmd5YW5neWU=,size_16,color_FFFFFF,t_70

[https://blog.csdn.net/henan_lujun/article/details/8984543]: https://blog.csdn.net/henan_lujun/article/details/8984543
[https://blog.csdn.net/muyuxuebao/article/details/51253204]: https://blog.csdn.net/muyuxuebao/article/details/51253204
