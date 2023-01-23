---
title: outlook登录腾讯企业邮箱 - 简书 
date: 2023-01-14 13:02  
tags: []  
source: https://www.jianshu.com/p/421c679b7eca
---
## outlook登录腾讯企业邮箱
## 腾讯企业邮箱设置
### 开启安全登录

在收发新设置中，需要确保开启IMAP/SMTP服务和开启POP/SMTP服务被勾选。  
如果发现无法勾选，需要联系邮箱管理员，在客户端收发信设置中将你的邮箱纳入白名单。
![][fig2]
![][fig3]
![][fig4]
### 获取第三方客户端登陆密码

在邮箱设置-邮箱绑定中，开启安全登录，然后点击生成新密码，获得客户端登陆密码（只显示一次，因此务必提前保持，当然忘了也不要紧，再申请一个就可以了）。

![][fig5]

## outlook邮箱登录

点击添加账户，输入邮箱名，并勾选手动设置
![][fig6]
![][fig7]

选择imap登录，并进行服务器设置:  
- 接收服务器：  imap.exmail.qq.com(使用SSL，端口号993)  
- 发送服务器：  smtp.exmail.qq.com(使用SSL，端口号465)
  

![][fig8]  
点击连接，输入上一步中的客户端登录密码，即可成功登录。

## reference
- [官方文档](https://service.exmail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1000564#2)

[fig1]: https://upload.jianshu.io/users/upload_avatars/19543241/90860e9b-bf90-4239-a86d-3619fe3eb045.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp
[fig2]: https://upload-images.jianshu.io/upload_images/19543241-6ba966648fbda710.png?imageMogr2/auto-orient/strip|imageView2/2/w/1086/format/webp
[fig3]: https://upload-images.jianshu.io/upload_images/19543241-bc89d24e1c49d54b.png?imageMogr2/auto-orient/strip|imageView2/2/w/1117/format/webp
[fig4]: https://upload-images.jianshu.io/upload_images/19543241-ca1a136ba9dee089.png?imageMogr2/auto-orient/strip|imageView2/2/w/1128/format/webp
[fig5]: https://upload-images.jianshu.io/upload_images/19543241-8d58bf9b85716406.png?imageMogr2/auto-orient/strip|imageView2/2/w/964/format/webp
[fig6]: https://upload-images.jianshu.io/upload_images/19543241-aab77c5d9a2072ec.png?imageMogr2/auto-orient/strip|imageView2/2/w/819/format/webp
[fig7]: https://upload-images.jianshu.io/upload_images/19543241-363311f843effbd6.png?imageMogr2/auto-orient/strip|imageView2/2/w/460/format/webp
[fig8]: https://upload-images.jianshu.io/upload_images/19543241-59945804bed176b7.png?imageMogr2/auto-orient/strip|imageView2/2/w/492/format/webp