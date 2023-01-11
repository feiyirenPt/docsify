---
title: jar打包  
date: 2022-11-14 22:27:40  
tags: java  
---

```bash
-c create
-e 指定主类
-v verbose
-f file

jar -cvef server/Main server.jar  .
创建包含多个发行版的 jar
jar --create --file mr.jar -C foo classes --release 9 -C foo9 classes
```
详见jar -h

带main-class的jar可直接用 `java -jar xxx.jar`执行
exe4j把jar打包成exe最高jdk11,结果必须带jre