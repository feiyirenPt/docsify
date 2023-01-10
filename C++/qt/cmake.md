title: proxy
date: 2022-10-11
tags:
- cmake
- windows
- MSVC
categories: [ coding ]
---
## MSVC cmake 指定C++版本
'''
if(MSVC)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++17 /Zc:__cplusplus")
endif(MSVC)
'''

set(CMAKE_PREFIX_PATH C:/Users/jyf/tool/Qt/install)

set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
