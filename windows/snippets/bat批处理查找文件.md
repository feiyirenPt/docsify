---
title: bat批处理查找文件  
date: 2023-02-24 10:08  
tags: bat  
---

# bat批处理查找文件

```bat
for /r . %i in (*.tex) do @echo %i
```