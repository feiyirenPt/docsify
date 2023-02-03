---
title: select多路复用  
date: 2022-10-19 22:21:22  
tags: C++  
---
> 首先我们先看一下最后一个参数。它指明我们要等待的时间，有如下三种情况：
> timeout == NULL  等待无限长的时间。等待可以被一个信号中断。当有一个描述符做好准备或者是捕获到一个信号时函数会返回。如果捕获到一个信号， select函数将返回 -1,并将变量 erro设为 EINTR。
> timeout->tv_sec == 0 &&timeout->tv_usec == 0不等待，直接返回。加入描述符集的描述符都会被测试，并且返回满足要求的描述符的个数。这种方法通过轮询，无阻塞地获得了多个文件描述符状态。
> timeout->tv_sec !=0 ||timeout->tv_usec!= 0 等待指定的时间。当有描述符符合条件或者超过超时时间的话，函数返回。在超时时间即将用完但又没有描述符合条件的话，返回 0。对于第一种情况，等待也会被信号所中断。
> [参考文献](https://blog.csdn.net/acs713/article/details/17531827)

但是实际测试下来select就算监视的套接字有变化也都返回0,没有返回套接字的个数,有待确认

```C++
     FD_ZERO(&reads);
     FD_SET(serv_sock, &reads);
     int fd_max = serv_sock;
     int fd_num;
     while (1) {
         cpy_reads = reads;
         timeout.tv_sec = 5000;
         timeout.tv_usec = 0;
         if ((fd_num = select(fd_max + 1, &cpy_reads, 0, 0, &timeout) == -1)) {
             break;
         }
         if (fd_num != 0) printf("select return %d\n", fd_num);
         // if (fd_num == 0) continue;
         for (int i = 0; i < fd_max + 1; i++) {
             if (FD_ISSET(i, &cpy_reads)) {
                 if (i == serv_sock) {
                     socklen_t adr_sz = sizeof(clnt_addr);
                     clnt_sock = accept(serv_sock, (struct sockaddr *)&clnt_addr,
                       &adr_sz);
                     FD_SET(clnt_sock, &reads);
                     if (fd_max < clnt_sock) {
                         fd_max = clnt_sock;
                     }
                     printf("connect client %d \n", clnt_sock);
                     } else {
                     int str_len = read(i, buf, BUF_SIZE);
                     if (str_len == 0) {
                         FD_CLR(clnt_sock, &reads);
                         close(i);
                         printf("disconnect client %d \n", i);
                     } else {
                         write(i, buf, str_len);
                     }
                 }
             }
         }
     }
     close(serv_sock);
```
