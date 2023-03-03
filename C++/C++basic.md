---
title: C++
date: 2022-10-11  
tags: C++  
---

- 一些宏定义
```C++
__FILE__  
__LINE__  
__DATE__  
__TIME__  
__FUNC__
__FUNCTION__
```

- [跨平台宏定义](https://stackoverflow.com/questions/5919996/how-to-detect-reliably-mac-os-x-ios-linux-windows-in-c-preprocessor)

```cpp
#ifdef _WIN64
   //define something for Windows (64-bit)
#elif _WIN32
   //define something for Windows (32-bit)
#elif __APPLE__
    #include "TargetConditionals.h"
    #if TARGET_OS_IPHONE && TARGET_OS_SIMULATOR
        // define something for simulator
        // (although, checking for TARGET_OS_IPHONE should not be required).
    #elif TARGET_OS_IPHONE && TARGET_OS_MACCATALYST
        // define something for Mac's Catalyst
    #elif TARGET_OS_IPHONE
        // define something for iphone  
    #else
        #define TARGET_OS_OSX 1
        // define something for OSX
    #endif
#elif __linux
    // linux
#elif __unix // all unices not caught above
    // Unix
#elif __posix
    // POSIX
#endif
```
