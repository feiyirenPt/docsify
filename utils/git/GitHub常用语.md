---
title: GitHub上常用语
date: 2023-01-27 17:36  
tags: [git]  
source: 
    - https://blog.csdn.net/weixin_38339817/article/details/124251886  
    - https://blog.csdn.net/weixin_44599143/article/details/128090981  
---

## LGTM、WIP等一类缩写
> 在看 GitHub 上 PR 回复的时候，往往会出现类似于 LGTM、WIP等一类缩写

通常，我们在 github 上最为常见的是以下这些词：

| 缩写 | 全拼 | 含义 |
| --- | --- | --- |
| PR | Pull Request | 如果给其它项目提交合并代码的请求时，就说会提交一个PR。 |
| WIP | Work In Progress | 如果你要做一个很大的改动，可以在完成部分的情况下先提交，但说明WIP，方便项目维护人员知道你还在 Work，同时他们可以先审核已经完成的。 |
| PTAL | Please Take A Look | 请求项目维护人员进行 code review。 |
| TBR | To Be Reviewed | 提示这些代码要进行审核。 |
| TL;DR | Too Long; Didn't Read | 太长了，懒得看。 |
| LGTM | Looks Good To Me | 通常是 code review 的时候回复的，即审核通过的意思。 |
| SGTM | Sounds Good To Me | 跟 LGTM 同义。 |
| AFAIK | As Far As I Know | 据我所知。 |
| CC | Carbon Copy | 抄送。 |


## git提交规范 fix,feat等字段含义
以下是commit提交规范，主要是在提交代码时标识本次提交的属性

```bash
feat: 新功能（feature）
fix: 修补bug
docs: 文档（documentation）
style: 格式（不影响代码运行的变动）
refactor: 重构（即不是新增功能，也不是修改bug的代码变动）
chore: 构建过程或辅助工具的变动
revert: 撤销，版本回退
perf: 性能优化
test：测试
improvement: 改进
build: 打包
ci: 持续集成
```