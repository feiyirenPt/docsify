---
title: (23 封私信 / 80 条消息) 小米手机用ADB卸载哪些软件不会卡米？ - 知乎  
date: 2023-01-28 14:52  
tags: [小米科技,米柚（MIUI）,小米手机]  
source: https://www.zhihu.com/question/512681245/answer/2320191705?utm_campaign=&utm_medium=social&utm_oi=1270684969300271104&~
---
## **[MIUI使用ADB彻底关闭系统级广告]**

## 1. 准备

MIUI 手机、Windows 电脑、数据线
**手机做好备份，以防万一**

**ADB 全称 Android Debug Bridge（**[Android 调试桥]），是一个通用命令行工具，可以与模拟器实例或连接的 Android 设备进行通信。


## 4. 进入开发者模式

打开设置→我的设备→全部参数→在 **MIUI 版本**上连续点击，直到提示 "您已处于开发者模式，无需进行此操作",然后打开**设置→**更多设置→开发者选项→向下拉勾选 **USB 调试**→弹出框点击确认

## 5. 连接手机与电脑

用数据线将手机与电脑连接，手机提示 “允许 USB 调试吗？” 点击确定即可

## 6. 使用 ADB 命令删除系统应用

卸载应用的命令为 `adb shell pm uninstall --user 0 <包名>` , 复制并将 `<包名>` 替换为你想要卸载的[应用包名]  
包名获取方法：长按应用图标，选择「ⓘ应用信息」，再点击右上角的「ⓘ」图标，里面有「应用包名」条目，长按该条目就复制了应用包名

```powershell
adb shell pm uninstall --user 0 com.miui.systemAdSolution（小米系统广告解决方案，必删）
adb shell pm uninstall --user 0 com.miui.analytics  （小米广告分析，必删）
adb shell pm uninstall --user 0 com.xiaomi.gamecenter.sdk.service  （小米游戏中心服务）
adb shell pm uninstall --user 0 com.xiaomi.gamecenter  （小米游戏中心）
adb shell pm uninstall --user 0 com.sohu.inputmethod.sogou.xiaomi  （搜狗输入法）
adb shell pm uninstall --user 0 com.baidu.input_mi （百度输入法小米版）
adb shell pm uninstall --user 0 com.miui.player  （小米音乐）
adb shell pm uninstall --user 0 com.miui.video  （小米视频）
adb shell pm uninstall --user 0 com.miui.notes  （小米便签）
adb shell pm uninstall --user 0 com.miui.translation.youdao  （有道翻译）
adb shell pm uninstall --user 0 com.miui.translation.kingsoft  （金山翻译）
adb shell pm uninstall --user 0 com.android.email  （邮件）
adb shell pm uninstall --user 0 com.xiaomi.scanner  （小米扫描）
adb shell pm uninstall --user 0 com.miui.hybrid  （混合器）
adb shell pm uninstall --user 0 com.miui.bugreport  （bug 反馈）
adb shell pm uninstall --user 0 com.milink.service  （米连服务）
adb shell pm uninstall --user 0 com.android.browser  （浏览器）
adb shell pm uninstall --user 0 com.miui.gallery  （相册）
adb shell pm uninstall --user 0 com.miui.yellowpage  （黄页）
adb shell pm uninstall --user 0 com.xiaomi.midrop  （小米快传）
adb shell pm uninstall --user 0 com.miui.virtualsim  （小米虚拟器）
adb shell pm uninstall --user 0 com.xiaomi.payment  （小米支付）
adb shell pm uninstall --user 0 com.mipay.wallet  （小米钱包）
adb shell pm uninstall --user 0 com.android.soundrecorder  （录音机）
adb shell pm uninstall --user 0 com.miui.screenrecorder  （屏幕录制）
adb shell pm uninstall --user 0 com.android.wallpaper  （壁纸）
adb shell pm uninstall --user 0 com.miui.voiceassist  （小爱同学）
adb shell pm uninstall --user 0 com.miui.fm  （收音机）
adb shell pm uninstall --user 0 com.miui.touchassistant  （悬浮球）
adb shell pm uninstall --user 0 com.android.cellbroadcastreceiver  （小米广播）
adb shell pm uninstall --user 0 com.xiaomi.mitunes  （小米助手）
adb shell pm uninstall --user 0 com.xiaomi.pass  （小米卡包）
adb shell pm uninstall --user 0 com.android.thememanager  （个性主题管理）
adb shell pm uninstall --user 0 com.android.wallpaper  （动态壁纸）
adb shell pm uninstall --user 0 com.android.wallpaper.livepicker  （动态壁纸获取）
```

另外，以下 APP 千万不要碰，除非你确定自己有可靠的救砖能力，不嫌麻烦，不怕数据丢失以及不追究我的责任:

【警告】以下系统自带应用删除后必定无法正常开机（来自网络），请避免误删：

```
com.miui.cloudservice  （小米云服务）
com.xiaomi.account  （小米账户）
com.android.updater （系统更新）
com.miui.cloudbackup  （云备份）
com.xiaomi.market  （应用市场）
```

**下面提供一些 MIUI 国际版（欧版** [miui.eu]**）应用包名（欧版可以随便删）：**

```
com.google.android.googlequicksearchbox （Google）
com.miui.miservice （服务与反馈）
com.mi.health （健康）
com.mi.globalbrowser （国际版浏览器）
com.miui.huanji （小米换机）
com.miui.newmidrive （小米云盘）
com.miui.bugreport （用户反馈）
com.miui.personalassistant （智能助理）
com.android.hotwordenrollment.xgoogle （谷歌助理1）
com.android.hotwordenrollment.okgoogle （谷歌助理2）
com.xiaomi.mirecycle （小米回收）
com.miui.videoplayer （小米视频国际版）
com.google.android.projection.gearhead （Google Auto/Google 汽车）
com.google.android.gms.location.history  （Google 地理位置历史记录）
com.google.ar.lens （Google 智能（虚拟）摄像头）
```

若在使用以上 adb 命令删除时出现「not installed for 0」错误，则可以尝试下面的命令：

**adb pm uninstall -k –user 0 package:<包名>**

另外，某个 APP 的包名可以通过长按图标，在属性中查看。在输入完上面的命令之后，长按该 APP 图标，选择「停止运行」、「停用」，就会发现这个应用的图标消失了。

[fig1]: https://pic1.zhimg.com/50/v2-80a4ff7ffd9413a88530d612ae002320_720w.jpg?source=1940ef5c
[MIUI使用ADB彻底关闭系统级广告]: https://link.zhihu.com/?target=https%3A//blog.tomys.top/2021-08/miui_ad/
[Android 调试桥]: https://link.zhihu.com/?target=https%3A//developer.android.com/studio/command-line/adb%3Fhl%3Dzh-cn
[MiFlash]: https://link.zhihu.com/?target=https%3A//www.xiaomiflash.com/
[应用包名]: https://www.zhihu.com/search?q=%E5%BA%94%E7%94%A8%E5%8C%85%E5%90%8D&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2320191705%7D
[云服务]: https://www.zhihu.com/search?q=%E4%BA%91%E6%9C%8D%E5%8A%A1&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2320191705%7D
[云备份]: https://www.zhihu.com/search?q=%E4%BA%91%E5%A4%87%E4%BB%BD&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2320191705%7D
[miui.eu]: https://link.zhihu.com/?target=https%3A//xiaomi.eu/
[CC BY-NC-SA 4.0 协议]: https://link.zhihu.com/?target=https%3A//creativecommons.org/licenses/by-nc-sa/4.0/
[https://blog.tomys.top/2021-08/miui\_ad/]: https://link.zhihu.com/?target=https%3A//blog.tomys.top/2021-08/miui_ad/