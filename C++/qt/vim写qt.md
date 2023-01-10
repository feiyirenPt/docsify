---
title: vim写qt
date: 2022-10-18 22:53:54
tags: qt
categories: coding
---
cmake命令
- 生成 compile_command.json
- 把qt由ui生成的mainwindow_ui.h加入到CMAKE_CXX_FLAGS让构建和clangd可以识别到
```
cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -DCMAKE_CXX_FLAGS=-I/home/jyf/untitled/build/untitled_autogen/include && make
```
