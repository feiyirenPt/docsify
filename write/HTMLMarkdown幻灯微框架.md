---
title: 敏捷你的PPT · 8 个开源 HTML/Markdown 幻灯微框架推荐  
date: 2023-02-06 20:28  
tags: [PPT分享,Markdown,HTML]  
source: https://zhuanlan.zhihu.com/p/100698434
---
这个世界上太多的 PPT 实际上**既不 Power，也没有 Point**。更可悲的是，一旦打开 PPT，我们就总忍不住妄图通过套用绚丽、专业的模板来**掩盖**这一点。

不是说 PPT 不应该追求美观、专业、有设计感，而是不应该本末倒置——如果只是在白色背景上用最朴素的文字罗列你的要点，你还好意思把它拿出来演讲吗？这是一个很好的**测试**，你不断精炼你的观点，直到它本身就已经闪闪发亮，然后再考虑锦上添花。也就是说**不要过早优化外观**。按照我们程序员的说法，这叫**迭代式**开发。

-   迭代1：构思演讲主题和章节名称。章节名称用二级标题。
-   迭代2：构思各章节要点，将要点书写在章节下面。
-   迭代3：各章节之间用 `---` 分隔，导入下面推荐的 HTML 幻灯模板中，自然就生成了一份朴实无华且枯燥但已经可进行演示的幻灯片。想象你用这份幻灯片进行演讲，是否足够吸引人？反复修改直至满意。
-   迭代4：准备重点章节的配图、图表等，插入幻灯片。
-   迭代5：重点、亮点内容精修样式。

本次推荐 8 个出色的开源 HTML/MD 幻灯微框架，推荐**原则**是：开源、免费、轻量、可离线演示，所以像 [slides.com] 、[gitpitch.com] 这种在线、收费的方案暂时不做介绍。


1.  remarkjs | 10k star  
    传送门：[Demo1] | [官方文档1] | [源码1]  
    追求极简的幻灯微框架，没有花哨的动效，不需要编译，直接修改 index.html 内嵌的 markdown，双击 index.html 就可进行演示。从幻灯编写到演示模式，所有功能都保持简单、快速、恰到好处。

![][fig1]

2. remark-it  
传送门：[Demo2] | [源码2]

remarkjs 虽好，但官方自带的主题和样式极少，remark-it 是一个使用 remarkjs 制作的开箱即用的幻灯模板，引入 typo.css、pure.css 等出色的开源样式库，可以节省大量编辑样式的时间。

特性：  
- Remarkjs 功能示例  
- 基于 Typo.css 的中英文排版  
- 基于 Pure.css 的多列布局  
- 基于 Nord 的暗色、亮色主题  
- 基于 Open color 的 150 个文字和背景颜色  
- 基于 Vue 的组件库

![][fig2]

![][fig3]

3. impress.js | 35k star

传送门：[Demo3] | [源码3]

非常酷炫的 3d CSS 动效，适合较为轻松的话题。

![动图封面][fig4]

4. Code Surfer | 4.5k star

传送门：[Demo4] | [Demo5] | [官方文档2] | [源码4]

非常直观的代码变更动效，适合做大量代码细节分享。

![动图][fig5]

5. reveal.js | 49k star

传送门：[Demo6] | [官方文档3] | [源码5]

技术大佬们都在用的幻灯框架。动效丰富，功能强大，适合愿意多花些时间制作出让人眼前一亮的作品的场景。

6. RISE | 2k star

传送门：[Demo7] | [官方文档4] | [源码6]

一个非常聪明的 Jupyter Notebook 插件。安装此插件后，只需要在现有的 Jupyter Notebook 的文档的 Cell 里选择幻灯页类型（幻灯片/子幻灯片/碎片/代码），按播放幻灯按钮就可以把 Jupyter Notebook 以类似 reveal.js 风格的幻灯片的形式来演示！

7. MDX Deck | 8k star

传送门：[Demo8] | [官方文档5] | [源码7]

用 React 制作幻灯片！优点是可以以MVVM模式做富交互组件。很适合用来在线演示 React 相关技术。

8. WebSlides | 5k star

传送门：[Demo9] | [Demo10] | [Demo11] | [官方文档6] | [源码8]

丰富的组件，时尚的样式，适合用来制作苹果发布会风格的幻灯。

[fig1]: https://pic1.zhimg.com/v2-930666c2d291144dfe29088124b281f0_b.jpg
[fig2]: https://pic3.zhimg.com/v2-9dc30a50bd00d583868f19217baee4ba_b.jpg
[fig3]: https://pic1.zhimg.com/v2-37a4607c26c0ba48db5dd1cdce142d2c_b.jpg
[fig4]: https://pic3.zhimg.com/v2-5c544ae2dbb5b7fd1a83346150199cb2_b.jpg
[fig5]: https://pic1.zhimg.com/v2-bce3e83fc4b5478ec18d573bdd20bb08_b.webp

[slides.com]: http://slide.com/
[gitpitch.com]: http://gitpitch.com/
[Demo1]: https://remarkjs.com/
[官方文档1]: https://github.com/gnab/remark/wiki
[源码1]: https://github.com/gnab/remark
[Demo2]: https://1-2-3.github.io/remark-it/
[源码2]: https://github.com/1-2-3/remark-it
[Demo3]: https://impress.js.org/
[源码3]: https://github.com/impress/impress.js
[Demo4]: https://advanced-graphql-workshop.netlify.com/
[Demo5]: https://react-conf-2018-hooks-intro.netlify.com/
[官方文档2]: https://codesurfer.pomb.us/
[源码4]: https://github.com/pomber/code-surfer
[Demo6]: https://revealjs.com/
[官方文档3]: https://github.com/hakimel/reveal.js/wiki
[源码5]: https://github.com/hakimel/reveal.js
[Demo7]: https://notebooks.gesis.org/binder/jupyter/user/damianavila-rise-5icrv0gh/notebooks/examples/README.ipynb
[官方文档4]: https://rise.readthedocs.io/en/maint-5.6/
[源码6]: https://github.com/damianavila/RISE
[Demo8]: https://mdx-deck.jxnblk.com/
[官方文档5]: https://mdxjs.com/
[源码7]: https://github.com/jxnblk/mdx-deck
[Demo9]: https://webslides.tv/
[Demo10]: https://webslides.tv/demos/components
[Demo11]: https://webslides.tv/demos/keynote
[官方文档6]: https://github.com/webslides/WebSlides/wiki
[源码8]: https://github.com/webslides/WebSlides
