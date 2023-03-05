---
title: socket tcp缓冲区大小的默认值、最大值 - 明明是悟空 - 博客园  
date: 2023-03-04 17:50  
tags: [C++,socket,buffer]  
source: https://www.cnblogs.com/x_wukong/p/8444557.html  
---

1 设置socket tcp缓冲区大小的疑惑

       疑惑1：通过setsockopt设置SO_SNDBUF、SO_RCVBUF这连个默认缓冲区的值，再用getsockopt获取设置的值，发现返回值是设置值的两倍。为什么？

        通过网上查找，看到linux的内核代码/usr/src/linux-2.6.13.2/net/core/sock.c，找到sock_setsockopt这个函数的这段代码：
```bash
      case SO_SNDBUF:
/* Don't error on this BSD doesn't and if you think about it this is right. Otherwise apps have to play 'guess the biggest size' games. RCVBUF/SNDBUF are treated in BSD as hints */
if (val  sysctl_wmem_max)//val是我们想设置的缓冲区大小的值
    val = sysctl_wmem_max;//大于最大值，则val值设置成最大值
    sk-sk_userlocks |= SOCK_SNDBUF_LOCK;
if ((val * 2) < SOCK_MIN_SNDBUF)//val的两倍小于最小值，则设置成最小值
    sk-sk_sndbuf = SOCK_MIN_SNDBUF;
else
    sk-sk_sndbuf = val * 2;//val的两倍大于最小值，则设置成val值的两倍
/*
*      Wake up sending tasks if we
*      upped the value.
*/
    sk-sk_write_space(sk);
    break;
case SO_RCVBUF:
/* Don't error on this BSD doesn't and if you think about it this is right. Otherwise apps have to play 'guess the biggest size' games. RCVBUF/SNDBUF are treated in BSD as hints */
if (val  sysctl_rmem_max)
    val = sysctl_rmem_max;
    sk-sk_userlocks |= SOCK_RCVBUF_LOCK;
/* FIXME: is this lower bound the right one? */
if ((val * 2) < SOCK_MIN_RCVBUF)
    sk-sk_rcvbuf = SOCK_MIN_RCVBUF;
else
    sk-sk_rcvbuf = val * 2;
    break;
```

?> 从上述代码可以看出：

?> 1. 当设置的值val  最大值sysctl_wmem_max，则设置为最大值的2倍：2*sysctl_wmem_max； 

?> 2. 当设置的值的两倍val*2  最小值，则设置成最小值：SOCK_MIN_SNDBUF；

?> 3. 当设置的值val < 最大值sysctl_wmem_max，且 val*2  SOCK_MIN_SNDBUF， 则设置成2*val。

```bash
查看linux 手册：
SO_RCVBUF：              
Sets or gets the maximum socket receive buffer in bytes.  
The kernel doubles this value to allow space for bookkeeping overhead) when is set using setsockopt(2), 
and this doubled value is returned by getsockopt(2).
The default value is set by the /proc/sys/net/core/rmem_default file, 
and the maximum allowed value is set by the /proc/sys/net/core/rmem_max file.  
The minimum (doubled) value for this option is 256.
```
```txt
查看我的主机Linux 2.6.6 ：/proc/sys/net/core/rmem_max：
4194304 //4M
查看/proc/sys/net/core/wmem_max：
8388608   //8M
```

**所以，能设置的接收缓冲区的最大值是8M，发送缓冲区的最大值是16M。**

疑惑2：为什么要有2倍这样的一个内核设置呢？我的理解是，用户在设置这个值的时候，可能只考虑到数据的大小，没有考虑数据封包的字节开销。所以将这个值设置成两倍。

> 注：overhead，在计算机网络的帧结构中，除了有用数据以外，还有很多控制信息，这些控制信息用来保证通信的完成。这些控制信息被称作系统开销。

2 tcp缓冲区大小的默认值

       建立一个socket，通过getsockopt获取缓冲区的值如下：

              发送缓冲区大小：SNDBufSize = 16384

              接收缓冲区大小：RCVBufSize = 87380 

        疑惑3：linux手册中，接收缓冲区的默认值保存在/proc/sys/net/core/rmem_default，发送缓冲区保存在/proc/sys/net/core/wmem_default。
```bash
[root@cfs_netstorage core]# cat /proc/sys/net/core/rmem_default
[root@cfs_netstorage core]# cat /proc/sys/net/core/wmem_default
```

        可知，接收缓冲区的默认值是：1048576，1M。发送缓冲区的默认值是：512488，512K。为什么建立一个socket时得到的默认值是87380、16384？？？

        进一步查阅资料发现， linux下socket缓冲区大小的默认值在/proc虚拟文件系统中有配置。分别在一下两个文件中：
```bash
/proc/sys/net/ipv4/tcp_wmem

[root@cfs_netstorage core]# cat /proc/sys/net/ipv4/tcp_wmem

4096    16384   131072  //第一个表示最小值，第二个表示默认值，第三个表示最大值。

/proc/sys/net/ipv4/tcp_rmem

[root@cfs_netstorage core]# cat /proc/sys/net/ipv4/tcp_rmem
```

       由此可见，新建socket，选取的默认值都是从这两个文件中读取的。可以通过更改这两个文件中的值进行调优，但是最可靠的方法还是在程序中调用setsockopt进行设置。通过setsockopt的设置，能设置的接收缓冲区的最大值是8M，发送缓冲区的最大值是16M（Linux 2.6.6中）。
