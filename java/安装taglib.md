---
title: 安装taglib
date: 2022-11-03 21:36:57
tags: java
categories: coding
---

[原文链接](https://blog.csdn.net/amiao_2018/article/details/116357125)

<!-- more -->
pom.xml
```xml
<dependency>
    <groupId>org.glassfish.web</groupId>
    <artifactId>jakarta.servlet.jsp.jstl</artifactId>
    <version>2.0.0</version>
</dependency>

<dependency>
    <groupId>org.apache.taglibs</groupId>
    <artifactId>taglibs-standard-spec</artifactId>
    <version>1.2.5</version>
</dependency>

// 如果不够,再补充下面这个依赖
<dependency>
    <groupId>org.apache.taglibs</groupId>
    <artifactId>taglibs-standard-impl</artifactId>
    <version>1.2.5</version>
</dependency>

```
并把maven依赖导入WEB-INF/lib
