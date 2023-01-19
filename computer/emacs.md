## windows下emacs + spacemacs

### 安装
```powershell
scoop install emacs
```
emacs在windows下的配置目录是`C:\Users\Administrator\AppData\Roaming\`

在上述路径下`git clone https://github.com/syl20bnr/spacemacs --depth=1`

然后编辑.emacs

```lisp
;; 设置emacs默认路径
(setq default-directory "~/") 
;; 加载自己的配置文件
(load-file "C:/Users/jyf/AppData/Roaming/.emacs.d/init.el")
```
- `M-m`这个地方其实是所有命令的总入口，分门别类了。  
所有emacs 的原命令基本都总结在这个 `M-m` 里了。
- `M-x`有时候不知道命令是啥，但就是想用，就可以 `M-x` 输入关键词，就能找到啦，例如 tex的时候需要清理临时文件，就可以输入 `tex clean` 就找到了`Tex-clean`命令，很体面。
- `C-c`主要是和buffer内容的mode相关的命令
- `C-x`主要是和内容无关的命令。


### 调整窗体大小
```lisp
;;设置窗口位置为屏库左上角(0,0)
(set-frame-position (selected-frame) 80 40)
;;设置宽和高,我的十寸小本是110,33,大家可以调整这个参数来适应自己屏幕大小
(set-frame-width (selected-frame) 120)
(set-frame-height (selected-frame) 25)
```
