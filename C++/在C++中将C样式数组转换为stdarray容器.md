---
created: 2023-01-09T17:16:29 (UTC +08:00)  
tags: [C++]    
source: https://www.techiedelight.com/zh/convert-c-style-array-into-std-array-container/  
---

# 在 C++ 中将 C 样式数组转换为 std::array 容器

> ## Excerpt
> 这篇文章将讨论如何在 C++ 中将 C 风格的数组转换为 std::array 容器... C++ 不提供从数组到 std::array 的任何直接转换。这是因为 `std::array` 类包含聚合类型并且没有自定义构造函数。

---
这篇文章将讨论如何在 C++ 中将 C 风格的数组转换为 std::array 容器。

C++ 不提供从数组到 `std::array`.这是因为 `std::array` 类包含聚合类型并且没有自定义构造函数。所以 `std::array` 可以使用类成员函数（例如复制、移动）或使用初始化列表来构造，否则每个元素都将被默认初始化。

## 1.使用 `std::copy` 或者 `std::n_copy` 功能

这个想法是将给定数组中的所有元素复制到 `std::array` 使用标准算法 `std::copy` 或者 `std::n_copy` 来自 `algorithm` 标题。如下所示：


[运行代码](https://www.techiedelight.com/zh/compiler/?run=nMfcEz)

## 2.使用 `std::move` 功能

我们也可以使用 `std::move` 代替 `std::copy`.如下所示：


[运行代码](https://www.techiedelight.com/zh/compiler/?run=1s3iLH)

## 3.使用 `reinterpret_cast` 功能

将给定数组中的所有元素复制到的另一种方法 `std::array` 是使用 `reinterpret_cast`.我们最好避免使用这个函数，因为 C++ 标准提供的保证很少 `reinterpret_cast` 行为。

以下代码有效，因为 `std::array` 类是 [POD(普通旧数据)类型](https://en.cppreference.com/w/cpp/named_req/PODType) 并且其内存布局要求与标准阵列相匹配。


[运行代码](https://www.techiedelight.com/zh/compiler/?run=UQtD6m)

这就是将 C 风格的数组转换为 `std::array` C++ 中的容器。

  

**谢谢阅读。**

请使用我们的 [在线编译器](https://www.techiedelight.com/zh/compiler/) 使用 C、C++、Java、Python、JavaScript、C#、PHP 和许多更流行的编程语言在评论中发布代码。

**像我们？将我们推荐给您的朋友，帮助我们成长。快乐编码** 🙂
