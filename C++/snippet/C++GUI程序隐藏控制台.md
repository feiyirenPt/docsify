---
title: C++GUI程序隐藏控制台  
date: 2023-02-18 16:40  
tags: C++  
---

# CGUI程序隐藏控制台

```cpp
#ifdef _WIN32
	HWND hwnd = GetForegroundWindow();
	if (hwnd) {
		ShowWindow(hwnd, SW_HIDE);
	}
#endif
```