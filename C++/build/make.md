---
title: Makefile
date: 2023-01-01 18:56:00
tags: make
categories: coding
---

```makefile
//Makefile
material=main.o hello.o
target=run
$(target):$(material)
	g++ $^ -o $@ && ./$@
%.o:%.cpp
	g++ $< -c
.PHONY: clean
clean:
	rm *.o run -f

```
```cpp
//hello.h
void hello();
```
```cpp
// hello.cpp
#include <iostream>
void hello(){
	std::cout << "main.h hello" << std::endl;	
}
```
```cpp
// main.cpp
#include <iostream>
#include "hello.h"

int main (int argc, char *argv[])
{
	hello();
	std::cout << "hello main" << std::endl;
	return 0;
}
```