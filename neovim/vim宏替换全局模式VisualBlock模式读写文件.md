---
title: vim【宏、替换、全局模式、Visual Block模式、读写文件】 - 简书  
date: 2023-01-20 10:33  
tags: []  
source: https://www.jianshu.com/p/3c34c189fc67
---
## vim【宏、替换、全局模式、Visual Block模式、读写文件】

[![][fig1]]

2020.01.31 15:25:53字数 1,758阅读 503

-   1.  命令的记录和回放
    
    -   1.  操作步骤：
        
        -   1.  `q{register}`命令：将后续的动作记录到名为`{register}`的寄存器中，其中给出的寄存器名字必须是`a`到`z`之间的一个字母。
        -   2.  执行你要执行的操作，按下`q`以结束对命令的记录。
        -   3.  `@{register}`命令：执行刚刚记录下来的宏。
    -   2.  例子：
        
        -   1.  `qa`：开始将后续的命令记入到寄存器`a`中。
        -   2.  将光标移动到行首。
        -   3.  `i#include "<Esc>`，在该行之前插入`#include`。
        -   4.  $将光标移动到行尾。
        -   5.  `a.h"<Esc>`：在行尾加上`.h"`字符。
        -   6.  `j`：移动到下一行。
        -   7.  `q`：停止记录。
        -   8.  `@a`：执行记录的宏，可以加计数命令。
        -   9.  `@@`：重复上一次宏的命令。
    -   3.  编辑宏的内容
        
        -   1.  `"ap`命令：显示宏的内容。
        -   2.  `"ad$`命令：将编辑好的宏的内容再一次的放入到寄存器中。
        -   3.  `qA`命令：向寄存器`a`中追加内容。
-   2.  替换
    
    -   1.  通用形式
        
        -   `:[range]submitute/from/to/[flags]`：对一个指定的范围执行替换操作，`range`指范围，`from`被替换的内容，与搜索命令所用的正则表达式类似，`to`替换为的内容，`flags`指一些常用的标记。
            -   如：`:s/the /these /g`，g是global的意思。
            -   如: `:s/one\two/one or two/g`
    -   2.  常用选项
        
        -   `range`：作用范围，`range=%`范围为所有行，而缺省只作用于当前行。
        -   `flags`：标记，`flags=g（global）`将改变一行所有符合目标字符串的全部字符进行替换。`flags=c`：在执行每个替换前请求用户确认`confirm`。
            -   `y`：好吧，yes。
            -   `n`：不，no。
            -   `a`：全部，all。
            -   `q`：退出，quit。
            -   `l`：把现在这个修改结束后进行退出。
            -   `CTRL-E`：向上滚屏一行。
            -   `CTRL-Y`：向下滚屏一行。
-   3.  命令的作用范围
    
    -   `:1,5s/this/that/g`：对第1行到第5行的文本执行替换操作。
    -   `:3s/this/that/g`：对指定行进行替换操作。
    -   `:.,$s/this/that/g`：当前行到最后一行范围，如：`$=1,$`。
    -   `:?^Chapter?,/^Chapter/s=this=that=g`：使用搜索模式来指定作用范围。
    -   `:?^Chapter?+1,/^Chapter/-1s=this=that=g`：增与减行的范围操作。
    -   `.+3,$-5s/this/that/g`：将当前行的下三行到倒数第6行的作用操作。
    -   `'t,'bs/this/that/g`：使用标记确定操作范围。
    -   `'<,'>s/this/that/g`：Visual模式确定的范围。
    -   `'>,$`：从上一次VIsual模式时选定的文本区域的结束处到文本末尾的这样的区域。
    -   `.,.+4`：`.`当前行到,`+4`从当前行到向下4行。
-   4.  全局命令
    
    -   `:[range]global/{pattern}/{command}`：找到符合某个匹配模式的行，然后将命令作用于这些行上，全局命令的默认作用范围是整个文件。
    -   `:g=//=s/foobar/barfoo/g`：整个文件中包含`//`的行，进行替换操作。
    -   `:g=//=d`：整个文件中包含`//`的行，进行删除操作。
-   5.  Visual Block模式
    
    -   1.  插入文本
        
        -   `Insert<Esc>`：在文本块的每行的行首，进行插入文本。
        -   `Astring<Esc>`：在文本块的每行的行尾，进行插入文本。
    -   2.  改变文本
        
        -   `cstring<Esc>`：修改文本块的文本，仅仅会修改文本块的内容。
        -   `Cstring<Esc>`：修改文本块的文本，会删除文本块尾部的内容。
    -   3.  改变文本的大小写
        
        -   `~`：交换大小写。
        -   `U`：将小写变大写。
        -   `u`：将大写变小写。
    -   4.  填充命令
        
        -   `rx`：以字符`x`进行文本块的填充操作。
    -   5.  左右移动
        
        -   `<`命令：会使你的文本向左移动一个shift单位。
        -   `>`命令：会使你的文本向右移动一个shift单位。
        -   `:set shiftwidth=4`：设置一个shift单位的宽度。
    -   6.  将多行内容粘贴起来
        
        -   `J`命令：使文本块纵跨的所有文本被连接为一行。
        -   `gJ`命令：如果你想要保留那些前导空白和后缀的空白时，可以使用。
-   6.  读写文件
    
    -   1.  读取文件
        
        -   `:read fileName`：读入文件的内容放在当前行。
        -   `$read fileName`：追加到文件的最后。
        -   `0read fileName`：把文件放在第一行的上面。
        -   `60read fileName`：那文件放在指定行的上面。
    -   2.  写入文件
        
        -   `:write fileName`：没有指定一个范围时该命令将写入整个文件的内容。
        -   `:.,$write fileName`：当前行到文件尾的内容写入文件，如果文件存在则失败。
        -   `:.,$write! fileName`：强制当前行到文件尾的内容写入文件，会进入覆盖模式。
        -   `:.write fileName`：将当前行写入文件中。
        -   `:.write >> fileName`：将当前行的内容追加到文件中。
    -   3.  格式化文本
        
        -   `:set textwidth`： 查看键入文字的时候每行的内容能自动调节到适应当前设置的宽度，每一行都会自动调整到只包含最多几个字符，Vim进行格式化文本的时候不会打断你的单词。
        -   `:set textwidth=100`： 设置键入文字的时候每行的内容能自动调节到适应当前设置的宽度，每一行都会自动调整到只包含最多`100`个字符，Vim进行格式化文本的时候不会打断你的单词。
        -   `:gqap`：`gq`为Vim的一个格式化操作符号，`ap`是一个文本对象，即：a paragraph。
        -   `gg gqG`：格式化整个文件的内容。
        -   `gqgq`：格式化当前行，可以与`.`重复命令一起使用。
        -   `gqj`：格式化当前行和它下面的一行。
    -   4.  改变大小写
        
        -   `guw`命令：`gu`是变小写的操作符，`w`是位移。
        -   `gUw`命令：`gU`是变大写的操作，`w`是位移。
        -   `g~w`命令：将字母的大小写进行反转，大写变小写，小写变大写。
        -   `gugu`命令：使一整行变为小写，简写为`guu`，同理`gUgU`、`gUU`、`g~g~`、`g~~`。
    -   5.  使用外部程序
        
        -   `sort < input.txt > output.txt`：
        -   `!5G`：`!`过滤操作符，`5G`为移动命令，决定了将哪个区域送到过滤程序中。
        -   `!!date`：`!!`命令为过滤当前行，`date`命令显示当前时间。
        -   `write !wc`：将文本写入一个命令`wc`中，`wc`命令是统计行数，单词数，字符数。

更多精彩内容，就在简书APP

"小礼物走一走，来简书关注我"

还没有人赞赏，支持一下

[![  ][fig2]]

总资产21共写了1.9W字获得40个赞共47个粉丝

### 推荐阅读[更多精彩内容]

-   官网 中文版本 好的网站 Content-type: text/htmlBASH Section: User ...
    
    [![][fig3]不排版]阅读 3,981评论 0赞 5
    
-   1\. 关于Vim vim是我最喜欢的编辑器，也是linux下第二强大的编辑器。 虽然emacs是公认的世界第一，我...
    
-   \[TOC\] ##Assoc 显示或修改文件扩展名关联 Assoc \[.Ext\[=\[Filetype\]\]\] .Ex...
    
-   vi(vim)可以说是linux中用得最多的工具了，不管你配置服务也好，写脚本也好，总会用到它。但是，vim作为一...
    
    [![][fig4]梁世勇]阅读 1,328评论 2赞 12
    
-   看完市场营销1-4班所有的搜索和投放渠道作业，有很多优秀的作业，为此，每个班保留了7-10个，大多投放渠道为知名的...
    
-   文/柳姑娘 关键词： 完美主义/偶像包袱/自我破碎 最早接触到这个词，是在工作第一个月的时候（没错，又是工作） 那...
    
-   1 江总深夜问我，西安下了这么大的雪，大作家不得写点什么。 我实在担不起“大作家”这个名号，但也会常常自嘲的在他面...
    
    [![][fig5]]

[fig1]: https://upload.jianshu.io/users/upload_avatars/8303589/2bdcf220-f9c5-4eba-a7c8-5667f443ea8b?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp
[fig2]: https://upload.jianshu.io/users/upload_avatars/8303589/2bdcf220-f9c5-4eba-a7c8-5667f443ea8b?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp
[fig3]: https://cdn2.jianshu.io/assets/default_avatar/4-3397163ecdb3855a0a4139c34a695885.jpg
[fig4]: https://cdn2.jianshu.io/assets/default_avatar/14-0651acff782e7a18653d7530d6b27661.jpg
[fig5]: https://upload-images.jianshu.io/upload_images/928511-c3d465eaa0103d1b.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240/format/webp

[![][fig1]]: https://www.jianshu.com/u/5d2ca1a95d0f
[![  ][fig2]]: https://www.jianshu.com/u/5d2ca1a95d0f
[更多精彩内容]: https://www.jianshu.com/
[![][fig3]不排版]: https://www.jianshu.com/u/97702e424c5d
[![][fig4]梁世勇]: https://www.jianshu.com/u/3bf4896b7fad
[![][fig5]]: https://www.jianshu.com/p/ecd92a397ee9
