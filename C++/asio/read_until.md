---
title: asio::read_until
date: 2023-02-04 21:42  
tags: [恼人的boost::asio::async_read_until]  
source:  
    - https://blog.csdn.net/iteye_20686/article/details/82451791  
    - http://www.cppblog.com/sunicdavy/archive/2012/12/03/195921.html  
---
## 恼人的boost::asio::async_read_until

### 问题
最近为服务器添加XMLSocket与Flash进行通信, 这种协议其实是一种以0结尾的字符串协议, 为了让asio兼容此协议, 我从文档找到了async_read_until异步读取系列, 这个函数的原理时, 给定一个streambuf, 和一个分隔符, asio碰到分隔符时返回, 你可以从streambuf中读取需要的数据. 看似很简单, 我很快写好一个demo与Flash进行通信, 结果发现在一个echo逻辑速度很快时, 服务器居然乱包了, 网上查了下, 官方原文是这样的:

> ```
> After a successful async_read_until operation, the streambuf may contain additional data beyond the delimiter. An application will typically leave that data in the streambuf for a subsequent async_read_until operation to examine.
> ```

### 解决方案
意思是, streambuf中并不一定是到分隔符前的所有数据, 多余的数据可能一样会在streambuf中. 也就是说, 还需要自己再次处理一遍数据...

动手呗, async_read_until看似就是一个废柴, 底层已经费了很多CPU在逐字符与分隔符的匹配上, 抛上来的数据居然还是半成品.

代码如下, 测试通过, 但是实在很费解为啥非要再做一次..

```cpp
boost::asio::streambuf* SB = SBP.get();
  // 访问缓冲  
const char* Buffs = boost::asio::buffer_cast<const char*>( SB->data() );
uint32 DataSize = 0;  
for ( uint32 i = 0; i < SB->size(); ++i ){  
    const char DChar = Buffs[i];
    // 这里需要自己判断字符串内容, read_until的文档里这么说的  
    if ( DChar == '0' )  {  
        DataSize = i;  
        break;  
    }  
}
if ( DataSize > 0 )  {  
    // 取成字符串  
    std::string FullText( Buffs, DataSize );  // 消费  
    SB->consume( DataSize );               
    mWorkService->post(  
        boost::bind(&AsioSession::NotifyReadString,  
        shared_from_this(),  
        FullText)  
    );
} 
```
!> 另外, 为了保证输入性安全, 可以在streambuf构造时加一个最大一个读取量, 超过此量会返回报错, 避免了缓冲区被撑爆的危险


## read_until配合正则表达式
- read_until 和 async_read_until如果要配合正则表达式得用boost版本
- head only 独立版本只能配合 `Char` `string` `string_view` `function`

## reference
[boost read_until]( http://www.boost.org/doc/libs/1_43_0/doc/html/boost_asio/reference/async_read_until/overload1.html ) 