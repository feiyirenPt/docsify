---
title: 编译qt源码
date: 2022-10-19 15:12:43
tags: qt
categories: [ coding ]
---
> [qt-doc](https://doc.qt.io/qt-6/windows-building.html)
> [参考资料](https://blog.csdn.net/skyloveka/article/details/108130252)
> [-static -static-runningtime](https://blog.csdn.net/piaopiaolanghua/article/details/118060886)
如果需要生成可执行文件不带dll,则需要静态编译qt,静态链接生成exe
# 环境
- MSVC (自带cmake ninja) 
- python 
- qt5开始不需要perl
# 编译命令(静态编译)
根据configure -h 进行裁剪 

```bash
..\qt-everywhere-src-6.4.0\configure -prefix ..\install -static -static-runtime -no-feature-androiddeployqt -skip qtimageformats,qtsvg,qtvirtualkeyboard,qtconnectivity -nomake examples -nomake tests -no-libjpeg -no-libpng -no-xcb -qt-sqlite  -platform win32-msvc -opengl desktop -release

cmake --build . --parallel
ninja install
```

最后在qtcreator里link qt(指定qmake)

[qt没有被正确的安装,请运行make install](https://blog.csdn.net/liukang325/article/details/53407401)