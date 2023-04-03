---
title: 配置项  
date: 2023-01-24 16:30  
tags: [docsify]  
---
注意创建`.nojekyll`,从而不忽略`_`开头的文件

github pages部署的时候
basePath不要乱动,默认就行
```js
window.$docsify = {
  basePath: '/path/',

  // 直接渲染其他域名的文档
  basePath: 'https://docsify.js.org/',

  // 甚至直接渲染其他仓库
  basePath:
    'https://raw.githubusercontent.com/ryanmcdermott/clean-code-javascript/master/',
};

```

## reference
[docsify](https://docsify.js.org/)