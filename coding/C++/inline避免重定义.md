---
title: c++ inline使函数实现可以在头文件中，避免多重定义错误 - ff_d - 博客园  
date: 2023-02-16 17:12  
tags: []  
source: https://www.cnblogs.com/l2017/p/10585700.html  
---
作者：Jon Lee  
链接：https://www.zhihu.com/question/53082910/answer/133612920  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

inline 绝对是C++里最让人混淆的关键词之一了（比static还过分）。

**\============== Update 30 Nov 2016**

看其他评论里有提到static 的。**个人评价一下 static + inline 一起：那就是把死人往活里搞，活人往死里搞的赶脚，坑之深简直不忍直视**。先上追加的3个结论；后面有代码，有耐心的小伙伴们拿回去自己试。

3\. **谨慎使用 static：如果只是想把函数定义写在头文件中，用 inline，不要用static。**static 和 inline 不一样：

-   static 的函数是 **internal linkage**。不同编译单元可以有同名的static 函数，但该函数**只对 对应的编译单元 可见**。如果同一定义的 static 函数，被不同编译单元调用，每个编译单元有自己**单独的****一份****拷贝，**且此拷贝**只对 对应的编译单元 可见。**
-   inline 的函数是 **external linkage**，如果被不同编译单元调用，每个编译单元引用／链接的是**同一函数，同一定义。**
-   上面的不同直接导致：如果函数内有 static 变量，**对inline 函数**，此变量对不同编译单元是**共享的**（Meyer's Singleton）；**对于static 函数，此变量不是共享的**。看后面的代码就明白区别了。

4\. static inline 函数，跟 static 函数单独没有差别，所以没有意义，只会混淆视听。

5\. inline 函数的**定义****不一定要跟声明放在一个头文件里面**：定义可以放在一个单独的头文件 .hxx 中，里面需要给函数**定义前加上 inline 关键字，原因看下面第 2.点；**然后声明 放在另一个头文件 .hh 中，此文件include 上一个 .hxx。这种用法 boost里很常见：优点1. 实现跟API 分离，encapsulation。优点2. 可以解决 有关inline 函数的 循环调用问题：这个不展开说了，看一个这个文章就懂了：[Headers and Includes: Why and How] 第 7 章，function inlining。

**Reference**: [inline specifier]

**\============== 原答案****30 Nov 2016**

1\. 不要再把 inline 和编译器优化挂上关系了，太误导人。编译器不傻，inline is barely a request。你不加inline，小函数在开O3时，编译器也会自动给你优化了。看到inline时，应该首先想到其他用意，在考虑编译器优化。

2\. inline最大的用处是：**非template 函数，成员或非成员**，把定义放在头文件中，定义前不加inline ，如果头文件被多个translation unit（cpp文件）引用，ODR会报错multiple definition。

**\============== static ／ inline 代码**

**a.hh**

<table><tbody><tr><td><p>1</p><p>2</p><p>3</p><p>4</p><p>5</p><p>6</p><p>7</p><p>8</p><p>9</p><p>10</p><p>11</p><p>12</p><p>13</p><p>14</p><p>15</p><p>16</p><p>17</p><p>18</p><p>19</p><p>20</p><p>21</p></td><td><div><p><code>#ifndef A_HH</code></p><p><code># define A_HH</code></p><p><code># include &lt;iostream&gt;</code></p><p><code>namespace</code> <code>static_test</code></p><p><code>{</code></p><p><code>&nbsp;&nbsp;</code><code>static</code> <code>int</code><code>&amp; static_value()</code></p><p><code>&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>static</code> <code>int</code> <code>value = -1;</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>return</code> <code>value;</code></p><p><code>&nbsp;&nbsp;</code><code>}</code></p><p><code>&nbsp;&nbsp;</code><code>namespace</code> <code>A</code></p><p><code>&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>set_value(</code><code>int</code> <code>val);</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>print_value();</code></p><p><code>&nbsp;&nbsp;</code><code>}</code></p><p><code>}</code></p><p><code>#endif</code></p></div></td></tr></tbody></table>

**a. cc**

<table><tbody><tr><td><p>1</p><p>2</p><p>3</p><p>4</p><p>5</p><p>6</p><p>7</p><p>8</p><p>9</p><p>10</p><p>11</p><p>12</p><p>13</p><p>14</p><p>15</p><p>16</p><p>17</p><p>18</p></td><td><div><p><code># include "a.hh"</code></p><p><code>namespace</code> <code>static_test</code></p><p><code>{</code></p><p><code>&nbsp;&nbsp;</code><code>namespace</code> <code>A</code></p><p><code>&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>set_value(</code><code>int</code> <code>val)</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code>auto</code><code>&amp; value = static_value();</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code>value = val;</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>}</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>print_value()</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code>std::cout &lt;&lt; static_value() &lt;&lt; </code><code>'\n'</code><code>;</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>}</code></p><p><code>&nbsp;&nbsp;</code><code>}</code></p><p><code>}</code></p></div></td></tr></tbody></table>

**b.hh:**

<table><tbody><tr><td><p>1</p><p>2</p><p>3</p><p>4</p><p>5</p><p>6</p><p>7</p><p>8</p><p>9</p><p>10</p><p>11</p><p>12</p><p>13</p><p>14</p><p>15</p></td><td><div><p><code>#ifndef B_HH</code></p><p><code># define B_HH</code></p><p><code># include &lt;iostream&gt;</code></p><p><code>namespace</code> <code>static_test</code></p><p><code>{</code></p><p><code>&nbsp;&nbsp;</code><code>namespace</code> <code>B</code></p><p><code>&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>set_value(</code><code>int</code> <code>val);</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>print_value();</code></p><p><code>&nbsp;&nbsp;</code><code>};</code></p><p><code>}</code></p><p><code>#endif</code></p></div></td></tr></tbody></table>

**b.cc:**

<table><tbody><tr><td><p>1</p><p>2</p><p>3</p><p>4</p><p>5</p><p>6</p><p>7</p><p>8</p><p>9</p><p>10</p><p>11</p><p>12</p><p>13</p><p>14</p><p>15</p><p>16</p><p>17</p><p>18</p><p>19</p></td><td><div><p><code># include "a.hh"</code></p><p><code># include "b.hh"</code></p><p><code>namespace</code> <code>static_test</code></p><p><code>{</code></p><p><code>&nbsp;&nbsp;</code><code>namespace</code> <code>B</code></p><p><code>&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>set_value(</code><code>int</code> <code>val)</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code>auto</code><code>&amp; value = static_value();</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code>value = val;</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>}</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>void</code> <code>print_value()</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>{</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code>std::cout &lt;&lt; static_value() &lt;&lt; </code><code>'\n'</code><code>;</code></p><p><code>&nbsp;&nbsp;&nbsp;&nbsp;</code><code>}</code></p><p><code>&nbsp;&nbsp;</code><code>}</code></p><p><code>}</code></p></div></td></tr></tbody></table>

**main. cc**

<table><tbody><tr><td><p>1</p><p>2</p><p>3</p><p>4</p><p>5</p><p>6</p><p>7</p><p>8</p><p>9</p><p>10</p><p>11</p><p>12</p><p>13</p><p>14</p><p>15</p><p>16</p><p>17</p></td><td><div><p><code># include "a.hh"</code></p><p><code># include "b.hh"</code></p><p><code>int</code> <code>main()</code></p><p><code>{</code></p><p><code>&nbsp;&nbsp;</code><code>static_test::A::set_value(42);</code></p><p><code>&nbsp;&nbsp;</code><code>static_test::A::print_value();</code></p><p><code>&nbsp;&nbsp;</code><code>static_test::B::print_value();</code></p><p><code>&nbsp;&nbsp;</code><code>static_test::B::set_value(37);</code></p><p><code>&nbsp;&nbsp;</code><code>static_test::A::print_value();</code></p><p><code>&nbsp;&nbsp;</code><code>static_test::B::print_value();</code></p><p><code>&nbsp;&nbsp;</code><code>return</code> <code>0;</code></p><p><code>}</code></p></div></td></tr></tbody></table>

-   a.hh 中标注 (!\*!) 的那行，**如果是inline**，输出：42，42，37，37。**value 在整个程序中是个Singleton**。
-   **如果是 static**，输出：42，－1，42，37。**value 在不同编译单元是不同的拷贝，即使它被标注 static**。

posted @ 2019-03-23 21:23  [ff\_d]  阅读(2252)  评论()  [编辑]  收藏  举报

[Headers and Includes: Why and How]: https://link.zhihu.com/?target=http%3A//www.cplusplus.com/forum/articles/10627/
[inline specifier]: https://link.zhihu.com/?target=http%3A//en.cppreference.com/w/cpp/language/inline
[ff\_d]: https://www.cnblogs.com/l2017/
[编辑]: https://i.cnblogs.com/EditPosts.aspx?postid=10585700
