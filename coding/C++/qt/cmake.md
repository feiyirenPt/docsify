title: proxy
date: 2022-10-11
tags:
- cmake
- windows
- MSVC
categories: [ coding ]
---
## MSVC cmake 指定C++版本
```
if(MSVC)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++17 /Zc:__cplusplus")
endif(MSVC)

set(CMAKE_PREFIX_PATH C:/Users/jyf/tool/Qt/install)

set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
```

## 手动处理ui文件
- 生成 `compile_command.json`
- 把qt由ui生成的`mainwindow_ui.h`加入到`CMAKE_CXX_FLAGS`让构建和clangd可以识别到

```bash
cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -DCMAKE_CXX_FLAGS=-I/home/jyf/untitled/build/untitled_autogen/include && make
```