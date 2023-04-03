---
title: easyx  
date: 2023-03-06 15:35  
tags: [C++,easyx]   
---

# easyx

### easyx 手动安装

![msvc easyx手动安装](https://blog.csdn.net/qq_35598074/article/details/110749803)

### xmake easyx
```lua
add_rules("mode.debug", "mode.release")
set_languages("c++20")
if is_plat("windows") then
	add_includedirs("C:/Users/jyf/tools/easyx/Include")
	add_linkdirs("C:/Users/jyf/tools/easyx/lib/VC2015/x64")
	add_links("shell32")
	add_links("User32")
	add_links("EasyXa")
	add_links("EasyXw")
end
target("easyx")
    set_kind("binary")
    add_files("*.cpp")

```