---
title: gcc 链接选项-static -static-libstdc++  
date: 2023-03-25 20:42  
tags: [C++]  
source: https://blog.csdn.net/leigelaile1/article/details/124952467  

---
当我们使用g++编译c++程序时，一般都会动态链接libstdc++.so共享库，有时候受限于不同机器和不同使用场景，我们希望静态链接libstdc++.so库，这样可能便于移植到相似的机器上，这时候就可以使用-static-xxx选项，将所有的库打包成一个可执行文件。他们之间的主要不同点在于：

- `-static`会将所以有用到的外部库全部以静态的方式链接

- `-static-libstdc++`只将`libstdc++.so`静态链接

- `-static-gcc` 同`-static-libstdc++`