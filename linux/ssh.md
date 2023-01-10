---
title: ssh
date: 2022-10-11
tags: ssh
categories: [ coding ]
---
## error ssh: connect to host github.com port 22: Connection timed out
```config
Host github.com
User 注册github的邮箱
Hostname ssh.github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
Port 443
```
[参考文章](https://blog.csdn.net/nightwishh/article/details/99647545)
## ssh公钥上传服务器
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_key

## SSH 命令的三种代理功能（-L/-R/-D） 
<!-- more -->
- 正向代理（-L）：相当于 iptable 的 port forwarding
- 反向代理（-R）：相当于 frp 或者 ngrok
- socks5 代理（-D）：相当于 ss/ssr

### 正向代理
所谓“正向代理”就是在本地启动端口，把本地端口数据转发到远端。
- 用法1：远程端口映射到其他机器
HostB 上启动一个 PortB 端口，映射到 HostC:PortC 上，在 HostB 上运行：
`HostB$ ssh -L 0.0.0.0:PortB:HostC:PortC user@HostC`
这时访问 HostB:PortB 相当于访问 HostC:PortC（和 iptable 的 port-forwarding 类似）。
- 用法2：本地端口通过跳板映射到其他机器
HostA 上启动一个 PortA 端口，通过 HostB 转发到 HostC:PortC上，在 HostA 上运行：
`HostA$ ssh -L 0.0.0.0:PortA:HostC:PortC  user@HostB`
这时访问 HostA:PortA 相当于访问 HostC:PortC。

- 两种用法的区别是，第一种用法本地到跳板机 HostB 的数据是明文的，而第二种用法一般本地就是 HostA，访问本地的 PortA，数据被 ssh 加密传输给 HostB 又转发给 HostC:PortC。

### 反向代理
所谓“反向代理”就是让远端启动端口，把远端端口数据转发到本地。
- HostA 将自己可以访问的 HostB:PortB 暴露给外网服务器 HostC:PortC，在 HostA 上运行:  
`HostA$ ssh -R HostC:PortC:HostB:PortB  user@HostC`
那么连接 HostC:PortC 就相当于链接 HostB:PortB。
*使用时需修改 HostC 的 /etc/ssh/sshd_config，添加：`GatewayPorts yes`*

相当于内网穿透，比如 HostA 和 HostB 是同一个内网下的两台可以互相访问的机器，HostC是外网跳板机，HostC不能访问 HostA，但是 HostA 可以访问 HostC
那么通过在内网 HostA 上运行 ssh -R 告诉 HostC，创建 PortC 端口监听，把该端口所有数据转发给我（HostA），我会再转发给同一个内网下的 HostB:PortB。
同内网下的 HostA/HostB 也可以是同一台机器，换句话说就是内网 HostA 把自己可以访问的端口暴露给了外网 HostC。
### 本地 socks5 代理
在 HostA 的本地 1080 端口启动一个 socks5 服务，通过本地 socks5 代理的数据会通过 ssh 链接先发送给 HostB，再从 HostB 转发送给远程主机：
`HostA$ ssh -D localhost:1080  HostB`
那么在 HostA 上面，浏览器配置 socks5 代理为 127.0.0.1:1080，看网页时就能把数据通过 HostB 代理出去，类似 ss/ssr 版本，只不过用 ssh 来实现。

 
### 使用优化
为了更好用一点，ssh 后面还可以加上：-CqTnN 参数，比如：
`$ ssh -CqTnN -L 0.0.0.0:PortA:HostC:PortC  user@HostB`
其中 -C 为压缩数据，-q 安静模式，-T 禁止远程分配终端，-n 关闭标准输入，-N 不执行远程命令。此外视需要还可以增加 -f 参数，把 ssh 放到后台运行。
这些 ssh 代理没有短线重连功能，链接断了命令就退出了，所以需要些脚本监控重启，或者使用 autossh 之类的工具保持链接。
### 功能对比
正向代理（-L）的第一种用法可以用 iptable 的 port-forwarding 模拟，iptable 性能更好，但是需要 root 权限，ssh -L 性能不好，但是正向代理花样更多些。反向代理（-R）一般就作为没有安装 frp/ngrok/shootback 时候的一种代替，但是数据传输的性能和稳定性当然 frp 这些专用软件更好。

socks5 代理（-D）其实是可以代替 ss/ssr 的，区别和上面类似。所以要长久使用，推荐安装对应软件，临时用一下 ssh 挺顺手。


[原文链接](https://www.cnblogs.com/cangqinglang/p/12732661.html)

## autossh

windows 下使用注意设置 ` $env:AUTOSSH_PATH=C:/Windows/System32/OpenSSH/ssh.exe`  
[参考链接](https://blog.csdn.net/weixin_30603633/article/details/96302754)  
`autossh -M 4000 -fCqTnNR {remote ip}:{port}:localhost:{port} {username}@{remote ip}`
- -M 指定监听连接的端口 
- -C 为压缩数据
- -q 安静模式
- -T 禁止远程分配终端
- -n 关闭标准输入
- -N 不执行远程命令
- -f 后台运行  
[参考资料](https://www.cnblogs.com/firstlady/p/15120212.html#:~:text=%E4%B8%BA%E4%BA%86%E6%9B%B4%E5%A5%BD%E7%94%A8%E4%B8%80%E7%82%B9%EF%BC%8Cssh%20%E5%90%8E%E9%9D%A2%E8%BF%98%E5%8F%AF%E4%BB%A5%E5%8A%A0%E4%B8%8A%EF%BC%9A%20-CqTnN%20%E5%8F%82%E6%95%B0%EF%BC%8C%E6%AF%94%E5%A6%82%EF%BC%9A%20ssh%20-CqTnN%20-D%200.0.,%E5%85%B3%E9%97%AD%E6%A0%87%E5%87%86%E8%BE%93%E5%85%A5%EF%BC%8C%20-N%20%E4%B8%8D%E6%89%A7%E8%A1%8C%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E3%80%82%20%E6%AD%A4%E5%A4%96%E8%A7%86%E9%9C%80%E8%A6%81%E8%BF%98%E5%8F%AF%E4%BB%A5%E5%A2%9E%E5%8A%A0%20-f%20%E5%8F%82%E6%95%B0%EF%BC%8C%E6%8A%8A%20ssh%20%E6%94%BE%E5%88%B0%E5%90%8E%E5%8F%B0%E8%BF%90%E8%A1%8C%E3%80%82)