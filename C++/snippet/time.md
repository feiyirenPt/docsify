---
title: time  
date: 2023-03-01 17:53  
tags:   
---

# time

```cpp
std::time_t t = std::time(nullptr);
std::tm *now = std::localtime(&t);

std::string ret;
ret += "[";
ret += std::to_string(now->tm_hour);
ret += ":";
ret += std::to_string(now->tm_min);
ret += ":";
ret += std::to_string(now->tm_sec);
ret += "]\n";
ret.append(result);
ret.append("\n");
return ret;
```