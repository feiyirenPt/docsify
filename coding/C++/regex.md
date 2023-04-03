---
title: C++正则表达式 - cpluspluser - 博客园  
date: 2023-03-29 23:09  
tags: [C++,regex]  
source: https://www.cnblogs.com/coolcpp/p/cpp-regex.html  
---

## 正则程序库（regex）

`正则表达式`就是一套表示规则的式子，专门用来处理各种复杂的操作。

std::regex是C++用来表示`正则表达式`(regular expression)的库，于C++11加入，它是`class std::basic_regex<>`针对char类型的一个特化，还有一个针对wchar_t类型的特化为std::wregex。

## 正则文法（regex syntaxes）

std::regex默认使用是ECMAScript文法，这种文法比较好用，且威力强大，常用符号的意义如下：

| 符号 | 意义                           |
| ---- | ------------------------------ |
| ^    | 匹配行的开头                   |
| $    | 匹配行的结尾                   |
| .    | 匹配任意单个字符               |
| […]  | 匹配[]中的任意一个字符         |
| (…)  | 设定分组                       |
|      | 转义字符                       |
| d    | 匹配数字[0-9]                  |
| D    | d 取反                         |
| w    | 匹配字母[a-z]，数字，下划线    |
| W    | w 取反                         |
| s    | 匹配空格                       |
| S    | s 取反                         |
| +    | 前面的元素重复1次或多次        |
| *    | 前面的元素重复任意次           |
| ?    | 前面的元素重复0次或1次         |
|      | 前面的元素重复n次              |
|      | 前面的元素重复至少n次          |
|      | 前面的元素重复至少n次，至多m次 |
|      |                                | 逻辑或 |

上面列出的这些都是非常常用的符号，靠这些便足以解决绝大多数问题了。

## 匹配（Match）

字符串处理常用的一个操作是「匹配」，即字符串和规则恰好对应，而用于匹配的函数为std::regex_match()，它是个函数模板，我们直接来看例子：

```cpp
std::regex reg("<.*>.*</.*>");
bool ret = std::regex_match("<html>value</html>", reg);

ret = std::regex_match("<xml>value<xml>", reg);

std::regex reg1("<(.*)>.*</1>");
ret = std::regex_match("<xml>value</xml>", reg1);

ret = std::regex_match("<header>value</header>", std::regex("<(.*)>value</1>"));

// 使用basic文法
std::regex reg2("<(.*)>.*</1>", std::regex_constants::basic);
ret = std::regex_match("<title>value</title>", reg2);
assert(ret);
```

对于语句中出现，是因为需要转义，C++11以后支持原生字符，所以也可以这样使用：

```
std::regex reg1(R"(<(.*)>.*</1>)");
auto ret = std::regex_match("<xml>value</xml>", reg1);
assert(ret);
```

但C++03之前并不支持，所以使用时要需要留意。

若是想得到匹配的结果，可以使用regex_match()的另一个重载形式：

```cpp
std::cmatch m;
auto ret = std::regex_match("<xml>value</xml>", m, std::regex("<(.*)>(.*)</(1)>"));
if (ret) {
    std::cout << m.str() << std::endl;
    std::cout << m.length() << std::endl;
    std::cout << m.position() << std::endl;
}

for (auto i = 0; i < m.size(); ++i) {
    std::cout << m[i].str() << " " << m.str(i) << std::endl;
}

for (auto pos = m.begin(); pos != m.end(); ++pos) {
    std::cout << *pos << std::endl;
}
```

`cmatch`是`class template std::match_result<>`针对C字符的一个特化版本，若是`string`，便得用针对`string`的特化版本`smatch`。同时还支持其相应的宽字符版本`wcmatch`和`wsmatch`。

在`regex_match()`的第二个参数传入`match_result`便可获取匹配的结果，在例子中便将结果储存到了cmatch中，而cmatch又提供了许多函数可以对这些结果进行操作，大多方法都和string的方法类似，所以使用起来比较容易。

m[0]保存着匹配结果的所有字符，若想在匹配结果中保存有子串，则得在「正则表达式」中用()标出子串，所以这里多加了几个括号：

```
std::regex("<(.*)>(.*)</(1)>")
```

这样这些子串就会依次保存在m[0]的后面，即可通过m[1],m[2],...依次访问到各个子串。

## 搜索（Search）

「搜索」与「匹配」非常相像，其对应的函数为std::regex_search，也是个函数模板，用法和regex_match一样，不同之处在于「搜索」只要字符串中有目标出现就会返回，而非完全「匹配」。

还是以例子来看：

```
std::regex reg("<(.*)>(.*)</(1)>");
std::cmatch m;
auto ret = std::regex_search("123<xml>value</xml>456", m, reg);
if (ret)
{
for (auto& elem : m)
std::cout << elem << std::endl;
}

std::cout << "prefix:" << m.prefix() << std::endl;
std::cout << "suffix:" << m.suffix() << std::endl;
```

输出为：

```
<xml>value</xml>
xml
value
xml
prefix:123
suffix:456
```

这儿若换成regex_match匹配就会失败，因为regex_match是完全匹配的，而此处字符串前后却多加了几个字符。

对于「搜索」，在匹配结果中可以分别通过prefix和suffix来获取前缀和后缀，前缀即是匹配内容前面的内容，后缀则是匹配内容后面的内容。

那么若有多组符合条件的内容又如何得到其全部信息呢？这里依旧通过一个小例子来看：

```
std::regex reg("<(.*)>(.*)</(1)>");
std::string content("123<xml>value</xml>456<widget>center</widget>hahaha<vertical>window</vertical>the end");
std::smatch m;
auto pos = content.cbegin();
auto end = content.cend();
for (; std::regex_search(pos, end, m, reg); pos = m.suffix().first)
{
std::cout << "----------------" << std::endl;
std::cout << m.str() << std::endl;
std::cout << m.str(1) << std::endl;
std::cout << m.str(2) << std::endl;
std::cout << m.str(3) << std::endl;
}
```

输出结果为：

```
----------------
<xml>value</xml>
xml
value
xml
----------------
<widget>center</widget>
widget
center
widget
----------------
<vertical>window</vertical>
vertical
window
vertical
```

此处使用了regex_search函数的另一个重载形式（regex_match函数亦有同样的重载形式），实际上所有的子串对象都是从std::pair<>派生的，其first（即此处的prefix）即为第一个字符的位置，second（即此处的suffix）则为最末字符的下一个位置。

一组查找完成后，便可从suffix处接着查找，这样就能获取到所有符合内容的信息了。

## 分词（Tokenize）

还有一种操作叫做「切割」，例如有一组数据保存着许多邮箱账号，并以逗号分隔，那就可以指定以逗号为分割符来切割这些内容，从而得到每个账号。

而在C++的正则中，把这种操作称为Tokenize，用模板类regex_token_iterator<>提供分词迭代器，依旧通过例子来看：

```
std::string mail("123@qq.vip.com,456@gmail.com,789@163.com,abcd@my.com");
std::regex reg(",");
std::sregex_token_iterator pos(mail.begin(), mail.end(), reg, -1);
decltype(pos) end;
for (; pos != end; ++pos)
{
std::cout << pos->str() << std::endl;
}
```

这样，就能通过逗号分割得到所有的邮箱：

```
123@qq.vip.com
456@gmail.com
789@163.com
abcd@my.com
```

sregex_token_iterator是针对string类型的特化，需要注意的是最后一个参数，这个参数可以指定一系列整数值，用来表示你感兴趣的内容，此处的-1表示对于匹配的正则表达式之前的子序列感兴趣；而若指定0，则表示对于匹配的正则表达式感兴趣，这里就会得到“,"；还可对正则表达式进行分组，之后便能输入任意数字对应指定的分组，大家可以动手试试。

## 替换（Replace）

最后一种操作称为「替换」，即将正则表达式内容替换为指定内容，regex库用模板函数std::regex_replace提供「替换」操作。

现在，给定一个数据为"he...ll..o, worl..d!"， 思考一下，如何去掉其中误敲的“.”？

有思路了吗？来看看正则的解法：

```
char data[] = "he...ll..o, worl..d!";
std::regex reg(".");
// output: hello, world!
std::cout << std::regex_replace(data, reg, "");
```

我们还可以使用分组功能：

```
char data[] = "001-Neo,002-Lucia";
std::regex reg("(d+)-(w+)");
// output: 001 name=Neo,002 name=Lucia
std::cout << std::regex_replace(data, reg, "$1 name=$2");
```

当使用分组功能后，可以通过$N来得到分组内容，这个功能挺有用的。

## 实例（Examples）

### 1. 验证邮箱

这个需求在注册登录时常有用到，用于检测用户输入的合法性。

若是对匹配精确度要求不高，那么可以这么写：

```
std::string data = "123@qq.vip.com,456@gmail.com,789@163.com,abcd@my.com";
std::regex reg("w+@w+(.w+)+");

std::sregex_iterator pos(data.cbegin(), data.cend(), reg);
decltype(pos) end;
for (; pos != end; ++pos)
{
std::cout << pos->str() << std::endl;
}
```

这里使用了另外一种遍历正则查找的方法，这种方法使用regex iterator来迭代，效率要比使用match高。这里的正则是一个弱匹配，但对于一般用户的输入来说没有什么问题，关键是简单，输出为：

```
123@qq.vip.com
456@gmail.com
789@163.com
abcd@my.com
```

但若我输入一个“Abc0_@aAa1.123.456.789”，它依旧能匹配成功，这明显是个非法邮箱，更精确的正则应该这样写：

```
std::string data = "123@qq.vip.com, 
       456@gmail.com, 
           789@163.com.cn.mail, 
           abcd@my.com, 
           Abc0_@aAa1.123.456.789 
           haha@163.com.cn.com.cn";
std::regex reg("[a-zA-z0-9_]+@[a-zA-z0-9]+(.[a-zA-z]+){1,3}");

std::sregex_iterator pos(data.cbegin(), data.cend(), reg);
decltype(pos) end;
for (; pos != end; ++pos)
{
std::cout << pos->str() << std::endl;
}
```

输出为：

```
123@qq.vip.com
456@gmail.com
789@163.com.cn.mail
abcd@my.com
haha@163.com.cn.com
```

## 2. 匹配IP

有这样一串IP地址，192.68.1.254 102.49.23.013 10.10.10.10 2.2.2.2 8.109.90.30，  
要求：取出其中的IP地址，并按地址段顺序输出IP地址。

有点晚了，便不详细解释了，这里直接给出答案，可供大家参考：

```
std::string ip("192.68.1.254 102.49.23.013 10.10.10.10 2.2.2.2 8.109.90.30");

std::cout << "原内容为：n" << ip << std::endl;

// 1. 位数对齐
ip = std::regex_replace(ip, std::regex("(d+)"), "00$1");

std::cout << "位数对齐后为：n" << ip << std::endl;

// 2. 有0的去掉
ip = std::regex_replace(ip, std::regex("0*(d{3})"), "$1");

std::cout << "去掉0后为：n" << ip << std::endl;

// 3. 取出IP
std::regex reg("s");
std::sregex_token_iterator pos(ip.begin(), ip.end(), reg, -1);
decltype(pos) end;

std::set<std::string> ip_set;
for (; pos != end; ++pos)
{
ip_set.insert(pos->str());
}

std::cout << "------n最终结果：n";

// 4. 输出排序后的数组
for (auto elem : ip_set)
{
// 5. 去掉多余的0
std::cout << std::regex_replace(elem, 
std::regex("0*(d+)"), "$1") << std::endl;
}
```

输出结果为：

```
原内容为：
192.68.1.254 102.49.23.013 10.10.10.10 2.2.2.2 8.109.90.30
位数对齐后为：
00192.0068.001.00254 00102.0049.0023.00013 0010.0010.0010.0010 002.002.002.002 008.00109.0090.0030
去掉0后为：
192.068.001.254 102.049.023.013 010.010.010.010 002.002.002.002 008.109.090.030
------
最终结果：
2.2.2.2
8.109.90.30
10.10.10.10
102.49.23.13
192.68.1.254
```
