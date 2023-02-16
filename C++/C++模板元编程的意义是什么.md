---
title: C++ 模板元编程的应用有哪些，意义是什么？_南方以北的博客-CSDN博客_模板元编程有什么用  
date: 2023-02-13 15:56  
tags: [模板元编程有什么用]  
source: https://blog.csdn.net/qq_25800311/article/details/99105434  
---
![][fig1]

[南方以北] ![][fig2] 于 2019-08-10 19:57:10 发布 ![][fig3] 1595 ![][fig4] 收藏 3

[https://www.cnblogs.com/liangliangh/p/4219879.html]

为了谈应用，先谈谈使命。模板元编程的根在模板。模板的使命很简单：为自动[代码生成]提供方便。提高程序员生产率的一个非常有效的方法就是“代码复用”，而面向对象很重要的一个贡献就是通过内部紧耦合和外部松耦合将“思想”转化成一个一个容易复用的“概念”。但是面向对象提供的工具箱里面所包含的继承，组合与多态并不能完全满足实际编程中对于代码复用的全部要求，于是模板就应运而生了。  
模板是更智能的宏。模板和宏都是编译前代码生成，像宏一样，模板代码会被编译器在编译的第一阶段（在内部转，这点儿与预编译器不同）就展开成合法的C++代码，然后根据展开的代码生成目标代码，链接到最终的应用程序之中。模板与宏相比，它站在更高的抽象层上面，宏操作的是字符串中的token，然而模板却能够操作C++中的类型。所以模板更加安全（因为有类型检查），更加智能（可以根据上下文自动特化）……  
说完模板，来说说模板元编程。模板元编程其实就是复杂点儿的模板，简单的模板在特化时基本只包含类型的查找与替换，这种模板可以看作是“类型安全的宏”。而模板元编程就是将一些通常编程时才有的概念比如：递归，分支等加入到模板特化过程中的模板，但其实说白了还是模板，自动代码生成而已。  
说完使命，来看看应用：编译时计算，补充类型系统，Domain Specific Language（是你说的“开发新语言”么？）  
编译时计算，比如拿模板来计算菲波纳切数列。优点是不占用运行时的CPU时间。但是这事儿吧，我觉得不该拿模板来搞，哪怕你拿python算好了再贴到C++文件里面，都比用模板好一点儿吧……还好C++11好像改了改这里，以后这种需求应该可以用constexpr来搞定了，那样会更好。  
补充类型系统，比如boost还是哪个的文档里面举的物理量计算的量纲问题。这个我觉得是非常有意义的，也是最有实用价值的。模板提供了参数化的类型，给我们一种来补充C++自带的类型系统的方法，使得类型系统更加智能与完备，很强大。  
DSL，我觉得用C++搞DSL不太好吧，有其它语言对DSL提供更易用的支持呀，比如scala, Haskell, Lisp……天涯何处无芳草，何必非跟C艹搞（我明明是C++脑残粉呀，似乎不能这么说吧，罪过罪过）……  
模板元编程缺点也是显而易见的，有人说它是C++里面的函数式编程语言，我觉得也有道理，维基百科上面说模板是图灵完全的，也就是理论上可以写出任何算法。然后这些信息综合一下儿就是尼玛命令式语言里面藏着一个函数式语言，一个编程语言里面放着另一个编程语言，这尼玛绝对是唯恐天下不乱的节奏呀！  
总而言之，这东西真有用，不信你出门问问，现在模板或宏已经成主流语言的标配了。但是这东西真的别乱用，想好了再用，码农何苦为难码农。如果你不觉得它有什么应用，就先别用。它不狭窄，是你还没看开……

___

简单来说，就四个大志：操纵类型。

虽然从形式上说，值也是类型。在Lambda Calculus中可以用![[公式]][fig5]表示值，在Lisp中可以用![[公式]][fig6]表示值。一个苹果是一，一个梨也是一。但是在C++中，值是受到歧视的。最简单的，我们不能用值重载。我们只能用劣质标签来匹配。但是我们可以用值来做模板参数（这是C++模板最重要的特性之一）。所以我们有Int Wrapper，用模板来把int包起来，这样我们就可以像使用类型一样使用值了。

关于操纵类型，最容易想到的就是type traits。什么两个类型能不能转换，在类型前面加减cv，加减指针加减引用，这都是最基本的类型的操作（这里有很多SFINAE的应用，但是SFINAE只是C++模板规则的一小部分，还不足以和模板元相提并论）。其实：

```
template <Template-Args>struct Function{using Type = ...;};
```

这就是一个接受类型（Template-Args）并返回类型（Type）的函数啊！在模板元编程中我们称呼这个东西为“元函数”。理解元函数就基本上理解模板元编程要干什么了。你有可能觉得模板元编程很弱欸，就这么个东西能图灵完备？当然了，因为我们还有偏特化（分支语句）和递归（循环语句），我们可以随意自如的处理类型。说到这，你还是不服，就几个破类型，YourClass，int，double，Int<N>，你还能给我玩出花来？

还真能。因为我们有这个：

```
template <typename A, typename B>struct Cons{using Car = A;using Cdr = B;};
```

我们可以`Cons<A, Cons<B, Cons<...>>>`无穷无尽也。有了Cons，就有了一切。二生三，三生万物。Cons就是二，那二怎么生三呢？简单：

```
template <typename K, typename L, typename R>using TreeNode = Cons<K, Cons<L, R>>;
```

有了线性结构、树状结构，有了偏特化、递归，我们为所欲为。

有了这些基础，我们再来体会一下高级的类型操纵。最简单的就是量纲分析了，量纲分析是《模板元编程》的开篇例子。模板元编程还有很多应用场景。**所有你需要存储、操纵、搜索类型的地方，都是模板元编程的用武之地。**

我们用一个例子结尾。假如我们需要做类型的映射，我们还需要用这些类型构造出对象。那么我们可以构造一颗编译期的平衡搜索树，存储这些（接收类型：返回类型）的映射。我们可以很方便地查找、获取、使用类型。如果你用一个哈希表存储类型名字的string的话，且不说效率低下的问题，查找获取类型当然也是可以的，但是得到的只是类型名字的string，如何使用这个类型呢？反射？很麻烦吧。

[fig1]: https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png
[fig2]: https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png
[fig3]: https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png
[fig4]: https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png
[fig5]: https://imgconvert.csdnimg.cn/aHR0cHM6Ly93d3cuemhpaHUuY29tL2VxdWF0aW9uP3RleD0lN0JmJTVDY2lyYytmJTVDY2lyYyslNUNjZG90cyslNUNjaXJjK2YlN0Q
[fig6]: https://imgconvert.csdnimg.cn/aHR0cHM6Ly93d3cuemhpaHUuY29tL2VxdWF0aW9uP3RleD0lN0IlMjglMjglMjklMjglMjklNUNjZG90cyUyOCUyOSUyOSU3RA

[南方以北]: https://stormzhou.blog.csdn.net/ "南方以北"
[https://www.cnblogs.com/liangliangh/p/4219879.html]: https://www.cnblogs.com/liangliangh/p/4219879.html
[代码生成]: https://so.csdn.net/so/search?q=%E4%BB%A3%E7%A0%81%E7%94%9F%E6%88%90&spm=1001.2101.3001.7020
