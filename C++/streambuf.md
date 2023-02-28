---
title: 关于C++之streambuf  
date: 2023-02-28 11:08  
tags: [C++,streambuf]  
source: https://blog.csdn.net/itzyjr/article/details/123642819  
---

## ❥关于C++之streambuf

![][fig2]

```cpp
typedef basic_streambuf<char> streambuf;typedef basic_streambuf<wchar_t> wstreambuf;
```

<streambuf>提供streambuf缓冲区类，与输入/输出流结合使用。

> 关于`streambuf`的资料并不多，IO Streams作者Jerry Schwarz这样说道：
> 
> 我最初设计的一个主要目标是以有趣的方式扩展它。特别是在流库中，streambuf类是一个实现细节，但在iostream库中，我希望它本身就是一个可用的类。我希望发布许多功能各异的streambuf。我自己写了一些，但几乎没有人写。我回答了“我如何使我的数字看起来像这样”的问题，而不是“我如何写一个streambuf”。教科书作者也倾向于忽略streambufs。显然，他们不同意我的观点，即输入/输出库的架构是一个有趣的案例研究。

实际的读写不是由流直接完成的，而是委托给流缓冲区。

流(streams)是[STL]里一个很重要的概念，例如`std::cin std::cout`用于终端的输入/输出。而实际上，真正的读/写操作并不是`stream`完成的，而是由`stream`调用`stream buffer`完成。

该模板被设计为处理窄字符(char类型)或宽字符([wchar_t]类型)的所有流缓冲区类的**虚基类**。

由于[虚基类]，因此没法直接创建。可以派生自己的子类，以便提供其他设备/数据输入的接口。

___

 每个流(`cout/cin/clog/ifstream/ofstream`)都有自己的流缓冲区(`streambuf`)。通过`rdbuf`接口可以获取当前的streambuf，也可以设置新的streambuf。

```cpp
get (1)streambuf* rdbuf() const;
set (2)streambuf* rdbuf(streambuf* sb);
第一种形式（1）返回指向当前与流关联的流缓冲区对象的指针。第二种形式（2）将sb指向的对象设置为与流关联的流缓冲区，并清除错误状态标志。
```

例如，我们可以修改`std::cout`和`std::stringstream`使用同一块缓冲区：

```cpp
#include <cstdio>
#include <iostream>
#include <sstream>
using namespace std;
int main() {
	stringstream ss;
	streambuf* cout_buf = cout.rdbuf();
	cout.rdbuf(ss.rdbuf());
	<!--使用了新的缓冲区后，字符串不会输出到屏幕，而是写入到stringstream-->
	cout << "std::cout 'hello world'";// don't print !!!
	printf("printf %s", ss.str().c_str());// 打印：printf std::cout 'hello world'
	std::cout.rdbuf(cout_buf);
	return 0;
}```

自定义缓冲区，详见：[https://izualzhy.cn/stream-buffer]

___

streambuf的两个子类stringbuf和filebuf，各看一个极简的示例：

```cpp
// stringbuf example
#include <string>
#include <iostream>
#include <sstream>// std::stringbuf
int main () {
  std::stringbuf buffer;// empty buffer
  std::ostream os(&buffer);// 关联stringbuf到os输出流
  <!--混合[输出到缓冲区]和[插入到关联流]-->
  // sputn(arg1,arg2)：arg1-指向要写入的字符序列的指针;arg2-要写入的字符数
  buffer.sputn("255 in hexadecimal: ", 20);
  os << std::hex << 255;
  std::cout << buffer.str();// 打印：255 in hexadecimal: ff
  return 0;
}```

```cpp
// filebuf example
#include <iostream>
#include <fstream>// std::filebuf
int main () {
  std::ifstream is;
  std::filebuf* fb = is.rdbuf();
  fb->open("test.txt", std::ios::in);
  if (fb->is_open())// 返回filebuf当前是否与文件关联
    std::cout << "the file is open.n";
  else
    std::cout << "the file is not open.n";
  fb->close();
  return 0;
}```

[fig2]: https://img-blog.csdnimg.cn/3f9b0b0898c043259cc6996e372ad36a.png