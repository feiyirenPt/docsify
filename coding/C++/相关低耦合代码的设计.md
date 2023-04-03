---
title: C/C++ 相关低耦合代码的设计_水火汪的博客-CSDN博客_c++降低耦合  
date: 2023-02-20 22:15  
tags: [c++降低耦合]  
source: https://blog.csdn.net/wanglei_11/article/details/128793675  
---
在我们设计C/C++ 程序的时候，有时需要两个类或者两个模块相互“认识”，或者两个模块间函数互相调用，假设我们正在开发一个网上商店，代表的网店客户的类必须要知道相关的账户。

[UML图]如下，这被称为环依赖，这两个类直接或间接地相互依赖。

![][fig1]

一般我们都会采用结构体或类前置声明的方式，在解决此问题。

customer.h
```cpp
#ifndef CUSTOMER_H_
#define CUSTOMER_H_
 
class Account;
class Customer
{
   // ...
   void setAccount(Account* account);
   {
       customerAccount = account;
   }
  //...
private:
   Account* customerAccount;
};
#endif
```

account.h
```cpp
#ifndef ACCOUNT_H_
#define ACCOUNT_H_
class Customer;
class Account
{
 public:
      //...
     void setOwer(Customer* customer)
     {
           ower = customer;
     }
   //...
  private:
         Customer* ower;
}
#endif```

老实说上面的方式确实可以消除编译器的错误，但是这种解决方案不够好。

下面的调用示例，存在一个问题，当删除Account的实例，Customer的实例仍然存在，且内部的指向Account的指针为空。使用或解引用此指正会导致严重的问题。

```cpp
#include "account.h"
#include "customer.h"
 
//...
Account *account = new Accout{};
Customer *customer = new Customer{};
account->setOwer(customer);
customer->setAccount(account);
```

那有没有更好的做法呢，`依赖倒置原则`可以很好的解决此类问题。

## 依赖倒置原则

第一步是我们不在两个类中的其中一个访问另一个，相反，我们只通过接口进行访问。我们从Customer中提取Ower的接口，作为示例，Ower接口中声明一个纯虚函数，该函数必须由此接口类覆盖。

ower.h
```cpp
#ifndef OWNER_H_
#define OWNER_H_
 
#include <memory>
#include <string>
 
class owner
{
   public:
       virtual ~owner()=default;
       virtual std::string getName() const = 0;
};
using OwnerPtr = std::shared_ptr<Owner>;
#endif
```

Customer.h
```cpp
#ifndef CUSTOMER_H_
#define CUSTOMER_H_
 
#include "Owner.h"
#include "Account.h"
 
class Customer:public Owner
{
  public:
     void setAccount(AccountPtr account)
     {
            customerAccount =   account;    
     }
  virtual std::string getName() const override{
    //return string
  }
 
  private:
     Account customerAccount;
};
using CustomerPtr = std::shared_ptr<Customer>;
#endif```

account.h
```cpp
#ifndef ACCOUNT_H_
#define ACCOUNT_H_
 
#include "Owner.h"
class Account
{
   public:
       void setOwner(OwnerPtr owner)
       {
          this->owner = owner;
       }
   private:
      OwnerPtr owner;
};
using AccountPtr = std::shared_ptr<Account>;```

现在设计完发现这两个模块间消除了环依赖。

## C/C++ 通过回调函数和信号槽的方式降低模块的耦合性

为了降低模块功能代码的耦合性，我们经常采用回调函数或者信号槽的方式来联系两个模块。

回调函数的方式：

a.h
```cpp
#pragma once
#ifndef A_H_
#define A_H_
#include <stdio.h>
 
 
int test(int c);
 
#endif
```

a.c
```cpp
#include "a.h"
int test(int c)
{
    c = 0x11112;
    return c;
}
```

b.h
```cpp
#pragma once
#ifndef B_H_
#define B_H_
#include <stdio.h>
 
typedef int (*PtrFunA)(int);
 
int testb(PtrFunA, int c);
#endif
```

b.c
```cpp
#include "b.h"
 
int testb(PtrFunA a, int c)
{
    int ret = a(c);
    printf("%d\n", ret);
    return ret;
}
```

main.c
```cpp
#include <stdio.h>
#include "a.h"
#include "b.h"
int main()
{
    testb(test,123);
}
```

这样做的好处降低代码的耦合性，是A模块的功能代码只写在A.C中。B.C的功能代码只写在B.C中，改进的后的回调函数可以用void*进行传参，在a.c中对void\进行判断，这是很多代码常做的操作。

信号槽的话则更加灵活性和代码的耦合度再次降低，后期在说，先写在这了。

[fig1]: https://img-blog.csdnimg.cn/img_convert/d5239aea9d7cb282949d5aef25af9f43.png
[fig2]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png
[fig3]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png
[fig4]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png
[fig5]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCodeMoreWhite.png
