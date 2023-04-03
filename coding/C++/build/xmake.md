---
title: xmake  
date: 2023-03-02 09:33  
tags: [C++,xmake]  
---

# xmake

- 切换编译选项

xmake.lua
```lua
add_rules("mode.debug", "mode.release")
```

```bash
xmake f -m debug
xmake f -m release
```