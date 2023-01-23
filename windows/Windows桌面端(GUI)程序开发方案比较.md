---
title: Windows桌面端(GUI)程序开发方案比较 | 码客  
date: 2023-01-22 19:41  
tags: [windows,GUI]  
source: https://www.psvmc.cn/article/2019-10-18-windows-program-develop.html
---
发表于 2019-10-18 | 分类于 [windows]

Windows桌面端程序开发方案比较(.NET Framework/.NET Core/.NET 5/6)

## 前言

先说结论

> 桌面端开发建议使用以下技术组合
> 
> -   Qt(C++) 性能高，效果好，跨平台，开发效率低(C++的锅)。
> -   WPF(C#) 性能适中，效果好，不跨平台，开发效率中等，占内存。
> -   Electron(NodeJS) 性能低，效果好，跨平台，开发效率高，占内存，三方库支持少。
> 
> 现在很多新应用都已经使用Electron来开发了，需要高性能的使用`node-ffi`调用原生即可。
> 
> 不建议使用Python+QT(或其他框架)来做客户端，我是使用了一段时间放弃了，打包大，性能也不高，关键是相关的文档也少，出现问题找解决方案都难。
> 
> 如果性能要求不高的应用建议使用Electron，性能要求高点的用WPF或Qt(C++)。

## Windows 下的 GUI 方案

Windows 下的 GUI 解决方案比较多：

-   基于 [C++] 的有 [Qt]、MFC、WTL、wxWidgets、DirectUI、Htmlayout；
-   基于 [C#] 的有 Winform、WPF；
-   基于Chromium和[Node.js]的[Electron]；
-   基于 [Java] 的有 AWT、[Swing]；
-   基于 Pascal 的 有Delphi；
-   基于[Go语言]的有 [walk]
-   还有国内初露头角的 [aardio]；
-   Visual Basic 曾经很流行，现在逐渐失去了色彩；

**现在常用的方案**

-   [Duilib+CEF] 只支持Windows的选择，优点是打包文件小（使用C++） QQ、微信、有道精品课。
-   Qt+CEF 支持跨平台，缺点是打包文件大（使用C++）。
-   WPF/(WPF+CEFSharp) 打包文件小，但是性能相比前两者弱，但比Electron强，内存占用高，只支持Windows。
-   Electron 打包文件大，但是性能弱，内存占用高，支持跨平台。

几种方案都各有利弊，可以根据团队的情况选用，都是相对不错的，其他的方案比如Flutter，Java就不太推荐。

## C++阵营

## QT和Duilib区别

Duilib是一款windows的下界面库，采用skia自绘的方式完成控件的显示，目前是开源状态，类似的控件库还有soui

而Qt则不是界面库那么简单，还包含有数据库，web，com通讯，tcpip通讯等等功能，应该称之为开发框架，并且包含了强大的ui系统。

Qt虽然开源，但是商业需要购买许可，duilib则不需要。

从稳定性上来说qt无疑是最为成熟和稳定的界面开发库，但是程序的运行依赖库较大，需要带上30~40M的qt基础库。

界面实现效果上两则区别不大，都可以实现比较丰富的界面外观，但是duilib的文档和资源较少，对开发人员的要求比较高。

此外如果涉及跨平台开发的话，duilib则无法胜任，只能支持windows下界面开发。

Qt自带的控件样式比较简单，可以通过qss进行控件美化，但是效果比较简单，这里可以尝试使用qt-ui界面库进行样式扩展，实现更加丰富的界面效果。

Qt-UI 是对qt控件的一种扩展，支持所有原生qt控件的接口和文档，可以帮助qt界面开发人员实现高质量的软件界面。

## QT的简介

常见的应用

-   Skype：一个使用人数众多的基于P2P的VOIP聊天软件
-   SMPlayer：跨平台多媒体播放器
-   Google地球（Google Earth）：三维虚拟地图软件
-   Autodesk Maya, 3D建模和动画软件
-   VirtualBox：虚拟机软件
-   YY语音
-   咪咕音乐
-   WPS Office

用 Qt 来开发 Windows 桌面程序有以下优点：

-   简单易学：Qt 封装的很好，几行代码就可以开发出一个简单的客户端，不需要了解 Windows API。
-   资料丰富：资料丰富能够成倍降低学习成本，否则你只能去看源码，关于 DirectUI、Htmlayout、aardio 的资料就很少。
-   漂亮的界面：Qt 很容易做出漂亮的界面和炫酷的动画，而 MFC、WTL、wxWidgets 比较麻烦。
-   独立安装：Qt 程序最终会编译为本地代码，不需要其他库的支撑，而 Java 要安装虚拟机，C# 要安装 .NET Framework。
-   跨平台：如果你的程序需要运行在多个平台下，同时又希望降低开发成本，Qt 几乎是必备的。

## 微软自家(Winform/WPF/UWP/WinUI)

微软家的技术就一个特点就是乱。一个又一个技术，一个出来另一个就被推翻，导致每一个技术都不是特别成熟。

[![image-20200813112012575][fig1]]

注意上图中

-   `.NET桌面开发`支持WinForm和WPF开发
-   `通用Windoes平台开发`支持UWP开发

请根据自身的需求安装

## Winform和WPF

WPF，即**windows presentation foundation**，windows呈现基础，属于**.net framework3.0**，是微软推出取代Winform的产品，能做到分离界面设计人员与开发人员的工作，提供多媒体交互用户图形界面，三大核心程序集是**presentationcore**、**presentationFramework**、**windowsBase**。

WPF和Winform最大的区别在于WPF底层使用的DirectX，Winform底层使用的是GDI+,所以WPF的图形界面上更胜一筹

-   GDI+(Graphics Device Interface)图形设备接口，它的主要任务是负责绘图程序之间的信息交换、处理，所有windows程序的图形输出
    
-   DirectX(Direct Extension)多媒体编程接口，加强3D图形和声音效果，有很多API组成。
    
    按照性质分类可分为四大部分：显示部分，声音部分，输入部分和网络部分
    

## WPF和UWP

**Universal Windows Platform (UWP)** 和 **Windows Presentation Foundation (WPF)** 是不相同的，虽然都可以做界面和桌面开发，但是 UWP 是一个新的 UI 框架，而且 UWP 是支持很多平台，至少比 WPF 多。

> UWP要求系统为Win10

那么 UWP 可以使用什么写？

-   xaml 的 UI 和 C#、VB 写的后台
-   xaml 的 UI 和 C++ Native 写的后台
-   DirectX 的 UI 和 C++ Native 写的后台
-   JavaScript 和 HTML

那么网上怎么好多小伙伴说 UWP 的性能比 WPF 好？

因为 UWP 的渲染使用的是 [DirectComposition] 而 WPF 使用的 Desktop Window

虽然 WPF 渲染是通过 Dx9 但是最后显示出来是需要 `Desktop Window Manager(DWM)`。

## WinUI

开发工具上默认是不能创建的，需要安装插件。不推荐。

## 怎么选择

WinForm和WPF之间肯定选择WPF，更灵活。

到底怎么选择WPF还是UWP？

> WPF是基于多窗口的，UWP是基于但窗口多Page的，这就决定了两者的开发跳转思想是不一致的，UWP就好似移动端开发一样，页面的跳转是基于导航的，所以只要应用有多窗口的需求就不要考虑UWP了。
> 
> 如果应用只考虑支持Win10，并且所有的功能都能通过内部跳转，类似于WEB应用或手机应用的交互，那么用UWP才是理想的选择，启动快，占用内存小

## .NET Framework和.NET Core及.NET 5/6

对比

| 技术             | 是否跨平台 | 特点                                                                      |
| ---------------- | ---------- | ------------------------------------------------------------------------- |
| `.NET Framework` | 否         | 只支持Windows 最新版本4.8，不再更新                                       |
| `.NET Core`      | 是         | 之前跨平台的方案，新建项目已经没有该选项，被`.NET 5/6`替代                |
| `.NET 5/6`       | 是         | `.NET Framework`和`.NET Core`的替代品，在依赖都有的情况下推荐使用该方式。 |

Visual Studio 2022创建WPF的两种方式

![image-20220901173830605][fig2]

这两种方式分别对应了

-   `.NET Framework`
-   `.NET 5/6`

已经不能选择`.NET Core`了.  
![image-20220901173830605][fig2]

[fig2]: https://image.psvmc.cn/blog/20220901173834.png

[windows]: https://www.psvmc.cn/categories/windows/
[C++]: http://c.biancheng.net/cplus/
[Qt]: http://c.biancheng.net/qt/
[C#]: http://c.biancheng.net/csharp/
[Node.js]: https://nodejs.org/
[Electron]: https://electronjs.org/
[Java]: http://c.biancheng.net/java/
[Swing]: http://c.biancheng.net/swing/
[Go语言]: http://c.biancheng.net/golang/
[walk]: https://github.com/lxn/walk
[aardio]: http://www.aardio.com/
[Duilib+CEF]: https://github.com/netease-im/NIM_Duilib_Framework/
[fig1]: http://image.psvmc.cn/blog/20200813112012.png!github
[DirectComposition]: https://msdn.microsoft.com/zh-cn/library/windows/desktop/hh437376.aspx
