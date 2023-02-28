---
title: C++中string如何实现字符串分割函数split()  
date: 2023-02-24 11:20  
tags: [c++,string,split]  
source: https://blog.csdn.net/weixin_43919932/article/details/111304250  
---
如：

```cpp
string str1 = "This is a test";
string str2 = "This-is-a-test";
string str2 = "This+is+a+test";
```

我们如何将以上字符串按照某种分隔符（　,`-`,`+`），将其分割成四个子串，其值分别为 “This” “is” “a” “test” 。

___

### 文章目录

-   -   -   [一、使用stringstream流]
        -   [二、使用string类提供的find方法与strsub方法]
        -   [三、使用C库函数strtok]
        -   [四、使用regex_token_iterator（正则表达式）]

### 一、使用[stringstream]流

这里我们只需要用到 `istringstream`（字符串输入流） 构造字符串流，然后从字符串流中**按照一定的格式**读取数据即可。

通常我们使用 **cin** 从流中读取数据，而我们也可以使用 **getline** 读取，而后者在读取时可以选择接受的数据格式，其函数原型如下：

```cpp
// istream & getline(char* buf, int bufSize);// 读到 n 为止
istream & getline(char* buf, int bufSize, char delim); //读到 delim 字符为止
// n 或 delim 都不会被读入 buf，但会被从文件输入流缓冲区中取走
```

因此，我们可以按照此方式设计一个C++中的string [split]函数。

```cpp
void Stringsplit(string str,const const char split)
{
    istringstream iss(str);// 输入流
    string token;// 接收缓冲区
    while (getline(iss, token, split))// 以split为分隔符
    {
        cout << token << endl; // 输出
    }
}
```

如果我们想要将分割后的子串带出，可以再重载一个有三个参数的版本。

```CPP
void Stringsplit(string str, const const char split,vector<string>& res)
{
    istringstream iss(str);// 输入流
    string token;// 接收缓冲区
    while (getline(iss, token, split))// 以split为分隔符
    {
        res.push_back(token);
    }
}
```

如此，我们就设计出了我们的Stringsplit() 函数。该函数有以下 2 种语法格式

```cpp
void Stringsplit(string str,const const char split);
// 默认将传入的字符串str以split为分隔符进行分割，并将得到的子串打印在屏幕上，无返回值
void Stringsplit(string str, const const char split,vector<string>& rst);
// 默认将传入的字符串str以split为分隔符进行分割，    不会将子串打印在屏幕上，无返回值
// 分割的子串将会保存在rst数组中被带出函数。
```

以上，我们简单的设计了一种C++中的分割字符串的函数，下面来看一个测试用例：

```cpp
string str("This is a test");
Stringsplit(str, ' ');// 打印子串

vector<string> strList;
string str2("This-is-a-test");
Stringsplit(str2, '-', strList);// 将子串存放到strList中
for (auto s : strList)
cout << s << " ";
cout << endl;

```

```bash
# 输出
This
is
a
test
This is a test
```

### 二、使用string类提供的find方法与strsub方法

函数原型：

```cpp
size_type find( const basic_string& str, size_type pos = 0 ) const;
```

参数  
str - 要搜索的 string ， pos - 开始搜索的位置  
返回值  
找到的子串的首字符位置，或若找不到这种子串则为 npos 。

函数原型：

```cpp
basic_string substr( size_type pos = 0, size_type count = npos ) const;
```

参数  
pos - 要包含的首个字符的位置 ，count - 子串的长度  
返回值  
含子串 [pos, pos+count) 的 string 。

由以上两个函数我们便可以设计出我们的Stringsplit()来。同时，因为find()函数查找的可以是字符串，因此我们的分隔符可以是单个的字符，也可以是一个字符串。

```cpp
// 使用字符分割
void Stringsplit(const string& str, const char split, vector<string>& res)
{
if (str == "")return;
//在字符串末尾也加入分隔符，方便截取最后一段
string strs = str + split;
size_t pos = strs.find(split);

// 若找不到内容则字符串搜索函数返回 npos
while (pos != strs.npos)
{
    string temp = strs.substr(0, pos);
    res.push_back(temp);
    //去掉已分割的字符串,在剩下的字符串中进行分割
    strs = strs.substr(pos + 1, strs.size());
    pos = strs.find(split);
}

    // 使用字符串分割
void Stringsplit(const string& str, const string& splits, vector<string>& res)
{
    if (str == "")return;
    //在字符串末尾也加入分隔符，方便截取最后一段
    string strs = str + splits;
    size_t pos = strs.find(splits);
    int step = splits.size();

    // 若找不到内容则字符串搜索函数返回 npos
    while (pos != strs.npos)
    {
        string temp = strs.substr(0, pos);
        res.push_back(temp);
        //去掉已分割的字符串,在剩下的字符串中进行分割
        strs = strs.substr(pos + step, strs.size());
        pos = strs.find(splits);
    }
}
```

下面是一个测试用例：

```cpp
int main()
{
    vector<string> strList;
    string str("This-is-a-test");
    Stringsplit(str, '-', strList);
    for (auto s : strList)
    cout << s << " ";
    cout << endl;

    vector<string> strList2;
    string str2("This%20is%20a%20test");
    Stringsplit(str2, "%20", strList2);
    for (auto s : strList2)
        cout << s << " ";
    cout << endl;
    return 0;
}
```

```bash
# 输出
This is a test
This is a test
```

### 三、使用C库函数strtok

```cpp
char* strtok( char* str, const char* delim );
```

参数  
str - 指向要记号化的空终止字节字符串的指针  
delim - 指向标识分隔符的空终止字节字符串的指针  
返回值  
指向下个记号起始的指针，或若无更多记号则为空指针。

需要注意的是，该函数使用一个全局的静态变量来保存每次分割后的位置，因此在多线程中是不安全的，这里我们也可以选择使用它的线程安全版本 `char *strtok_r(char *str, const char *delim, char **saveptr);` 。

```cpp
void Stringsplit(const string& str, const string& split, vector<string>& res)
{
    char* strc = new char[str.size() + 1];
    strcpy(strc, str.c_str());   // 将str拷贝到 char类型的strc中
    char* temp = strtok(strc, split.c_str());
    while (temp != NULL)
    {
        res.push_back(string(temp));
        temp = strtok(NULL, split.c_str());// 下一个被分割的串
    }
    delete[] strc;
}
```

如此，我们的使用 **strtok** 版本的Stringsplit() 就完成了。不过，我们使用这种方法实现的字符串分割函数只能根据字符来分割，而我们传入的参数是字符串类型，这样可能会对函数的使用这造成误导（注：参数传入字符串用的双引号，传入字符用的单引号），因此我们也可以使用下面的方法封装一个参数是字符类型的函数。

```cpp
void Stringsplit(const string& str, const char split, vector<string>& res)
{
    Stringsplit(str, string(1,split), res);// 调用上一个版本的Stringsplit()
}
```

下面给出一个测试用例，我们分别使用单/双引号传入分割的限定字符。

```cpp
int main()
{
    vector<string> strList;
    string str("This+is+a+test");
    Stringsplit(str, '+', strList);
    for (auto s : strList)
        cout << s << " ";
    cout << endl;

    vector<string> strList2;
    string str2("This-is-a-test");
    Stringsplit(str2, "-", strList2);
    for (auto s : strList2)
        cout << s << " ";
    cout << endl;
    return 0;
}
```

```bash
# 输出
This is a test
This is a test
```

### 四、使用regex_token_iterator（正则表达式）

> 正则表达式(regular expression)描述了一种字符串匹配的模式（pattern），可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。

而在C++的正则中，把这种操作称为Tokenize分词（或者叫切割）。这种操作刚好可以满足我们的需求，用模板类regex_token_iterator<>提供分词迭代器，可以完成字符串的分割。

> 有关C++正则表达式参考：[C++ std::regex | 正则表达式]

代码参考：

```cpp
void Stringsplit(const string& str, const string& split, vector<string>& res)
{
    //std::regex ws_re("s+"); // 正则表达式,匹配空格 
    std::regex reg(split);// 匹配split
    std::sregex_token_iterator pos(str.begin(), str.end(), reg, -1);
    decltype(pos) end;              // 自动推导类型 
    for (; pos != end; ++pos)
    {
        res.push_back(pos->str());
    }
}
```

测试用例：

```cpp
int main()
{
    // 单个字符分词
    vector<string> strList;
    string str("This is a test");
    Stringsplit(str," ", strList);
    for (auto s : strList)
        cout << s << " ";
    cout << endl;

    // 使用字符串分词
    vector<string> strList2;
    string str2("ThisABCisABCaABCtest");
    Stringsplit(str2, "ABC", strList2);
    for (auto s : strList2)
        cout << s << " ";
    cout << endl;
}
```

```bash
# 输出
This is a test
This is a test
```

[一、使用stringstream流]: https://blog.csdn.net/weixin_43919932/article/details/111304250#stringstream_13
[二、使用string类提供的find方法与strsub方法]: https://blog.csdn.net/weixin_43919932/article/details/111304250#stringfindstrsub_87
[三、使用C库函数strtok]: https://blog.csdn.net/weixin_43919932/article/details/111304250#Cstrtok_176
[四、使用regex_token_iterator（正则表达式）]: https://blog.csdn.net/weixin_43919932/article/details/111304250#regex_token_iterator_240
[stringstream]: https://so.csdn.net/so/search?q=stringstream&spm=1001.2101.3001.7020
[split]: https://so.csdn.net/so/search?q=split&spm=1001.2101.3001.7020
[C++ std::regex | 正则表达式]: https://blog.csdn.net/weixin_43919932/article/details/123947174
