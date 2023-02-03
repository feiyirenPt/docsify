---

title: Linux下使用acme.sh 配置https 免费证书
date: 2023-01-23 22:57  
tags: [linux,acme,cert]  
source: https://www.cnblogs.com/-mrl/p/10601817.html

---

# acme.sh

> 简单来说acme.sh 实现了 acme 协议, 可以从 let‘s encrypt 生成免费的证书。  
> acme.sh 有以下特点：  
> 一个纯粹用Shell（Unix shell）语言编写的ACME协议客户端。  
> 完整的ACME协议实施。 支持ACME v1和ACME v2 支持ACME v2通配符证书  
> 简单，功能强大且易于使用。你只需要3分钟就可以学习它。  
> Let's Encrypt免费证书客户端最简单的shell脚本。  
> 纯粹用Shell编写，不依赖于python或官方的Let's Encrypt客户端。  
> 只需一个脚本即可自动颁发，续订和安装证书。 不需要root/sudoer访问权限。  
> 支持在Docker内使用，支持IPv6
> github链接：[https://github.com/Neilpang/acme.sh]

**本文记录了我在把网站从HTTP升级到 HTTPS ，申请和安装SSL证书路上踩过的几个坑。**

**安装环境：**  
**操作系统：centos 7 X64**  
**SSL证书来源：Let's Encrypt**  
**安装用脚本：acme.sh**  
**服务器：nginx**  
**域名：chandao.test.com**

1.安装acme.sh

```bash
curl https://get.acme.sh | sh
```

2.安装后的配置  
把 acme.sh 安装到你的 home 目录下:~/.acme.sh/并创建 一个 bash 的 alias, 方便你的使用:

```bash
alias acme.sh=~/.acme.sh/acme.sh
echo 'alias acme.sh=~/.acme.sh/acme.sh' >>/etc/profile
```

安装过程中会自动为你创建 cronjob, 每天 0:00 点自动检测所有的证书, 如果快过期了, 需要更新, 则会自动更新证书(可执行crontab -l 查看)。

```bash
00 00 * * * root /root/.acme.sh/acme.sh --cron --home /root/.acme.sh &>/var/log/acme.sh.logs
```

3.申请证书  
acme.sh 实现了 acme 协议支持的所有验证协议. 一般有两种方式验证: http 和 dns 验证（本文不提供dns方式申请，dns手动模式，不能自动更新证书。在续订证书时，您必须手动向域中添加新的txt记录。）

HTTP 方式方法如下：

```bash
acme.sh --issue -d chandao.test.com --webroot /data/wwwroot/chandao
```

只需要指定域名, 并指定域名所在的网站根目录【命令中/data/wwwroot/chandao为域名的根目录路径】. acme.sh 会全自动的生成验证文件, 并放到网站的根目录, 然后自动完成验证. 最后会聪明的删除验证文件. 整个过程没有任何副作用.

4.证书的安装  
注意, 默认生成的证书都放在安装目录下: ~/.acme.sh/, 请不要直接使用此目录下的文件,  
例如: 不要直接让 nginx/apache 的配置文件使用这下面的文件.  
这里面的文件都是内部使用, 而且目录结构可能会变化.

正确的使用方法是使用 --installcert 命令,并指定目标位置, 然后证书文件会被copy到相应的位置,

默认情况下，证书将每60天更新一次（可配置）。更新证书后，将通过以下命令自动重新加载Apache / Nginx服务：`service apache2 force-reload`或`service nginx force-reload`。

请注意：reloadcmd非常重要。证书可以自动续订，但是，如果没有正确的“reloadcmd”，证书可能无法刷新到您的服务器（如nginx或apache），那么您的网站将无法在60天内显示续订证书。

nginx示例1:

```
acme.sh --installcert -d chandao.test.com --key-file /usr/local/nginx/ssl_cert/test.com/chandao.test.com.key --fullchain-file /usr/local/nginx/ssl_cert/test.com/chandao.test.com.cer --reloadcmd "service nginx force-reload"
```

nginx示例2：

```bash
acme.sh --install-cert -d chandao.test.com \
--key-file /usr/local/nginx/ssl_cert/test.com/chandao.test.com.key \
--fullchain-file /usr/local/nginx/ssl_cert/test.com/chandao.test.com.cer \
--reloadcmd      "service nginx force-reload"
```

apache示例：

```bash
acme.sh --install-cert -d chandao.test.com \
--cert-file /usr/local/nginx/ssl_cert/test.com/chandao.test.com.key \
--key-file /path/to/keyfile/in/apache/key.pem \
--fullchain-file /usr/local/nginx/ssl_cert/test.com/chandao.test.com.cer \
--reloadcmd      "service apache2 force-reload"
```

附带完成前面1-4步骤的截图：

![][fig1]

5. Nginx/Tengine服务器安装SSL证书

Nginx 配置Http和Https共存

![复制代码][fig2]

```
listen 80; #如果硬性要求全部走https协议，这一行去除
listen 443 ssl http2; #如果硬性要求全部走https协议，这里去除ssl
server_name chandao.test.com;

#ssl on; #如果硬性要求全部走https协议，这里开启ssl on
ssl_certificate /usr/local/nginx/ssl_cert/test.com/chandao.test.com.cer;
ssl_certificate_key /usr/local/nginx/ssl_cert/test.com/chandao.test.com.key;

#ssl性能调优
#nginx 1.13.0支持了TLSv1.3,TLSv1.3相比之前的TLSv1.2、TLSv1.1等性能大幅提升
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5;
ssl_prefer_server_ciphers on;
ssl_session_timeout 10m;
#使用ssl_session_cache优化https下Nginx的性能
ssl_session_cache builtin:1000 shared:SSL:10m;
#OCSP Stapling 开启。OCSP是用于在线查询证书吊销情况的服务，使用OCSP Stapling能将证书有效状态的信息缓存到服务器，提高 TLS 握手速度
ssl_stapling on;
#OCSP Stapling 验证开启
ssl_stapling_verify on; 
```

![复制代码][fig3]

完整例子：

![复制代码][fig4]

```conf
server {
  listen 80;  #如果硬性要求全部走https协议，这一行去除
  listen       443 ssl http2;    #如果硬性要求全部走https协议，这里去除ssl
  server_name chandao.test.com;
  access_log off;
  index index.html index.htm index.php;
  root /data/wwwroot/chandao;

  #ssl on;   #如果硬性要求全部走https协议，这里开启ssl on
  ssl_certificate   /usr/local/nginx/ssl_cert/test.com/chandao.test.com.cer;
  ssl_certificate_key  /usr/local/nginx/ssl_cert/test.com/chandao.test.com.key;

  #ssl性能调优
  #nginx 1.13.0支持了TLSv1.3,TLSv1.3相比之前的TLSv1.2、TLSv1.1等性能大幅提升
  ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
  ssl_ciphers EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5;
  ssl_prefer_server_ciphers on;
  ssl_session_timeout 10m;
  #使用ssl_session_cache优化https下Nginx的性能
  ssl_session_cache builtin:1000 shared:SSL:10m;
  #OCSP Stapling 开启。OCSP是用于在线查询证书吊销情况的服务，使用OCSP Stapling能将证书有效状态的信息缓存到服务器，提高 TLS 握手速度
  ssl_stapling on;
  #OCSP Stapling 验证开启
  ssl_stapling_verify on; 

  #error_page 404 /404.html;
  #error_page 502 /502.html;

  location ~ [^/]\.php(/|$) {
    #fastcgi_pass remote_php_ip:9000;
    fastcgi_pass unix:/dev/shm/php-cgi.sock;
    fastcgi_index index.php;
    include fastcgi.conf;
  }

  location ~ .*\.(gif|jpg|jpeg|png|bmp|swf|flv|mp4|ico)$ {
    expires 30d;
    access_log off;
  }
  location ~ .*\.(js|css)?$ {
    expires 7d;
    access_log off;
  }
  location ~ /\.ht {
    deny all;
  }
}
```

6.重启nginx  
保存退出后，通过nginx -t来检查配置文件是否正确，有错误的话改之即可。配置文件检测正确之后，通过service nginx force-reload来重载配置文件。

```bash
nginx -t
service nginx force-reload
```

7. 更新 acme.sh  
   目前由于 acme 协议和 letsencrypt CA 都在频繁的更新, 因此 acme.sh 也经常更新以保持同步.

升级 acme.sh 到最新版 :

如果你不想手动升级, 可以开启自动升级:

```bash
acme.sh --upgrade --auto-upgrade
```

之后, acme.sh 就会自动保持更新了.

你也可以随时关闭自动更新:

```bash
acme.sh --upgrade --auto-upgrade 0
```

6. 出错怎么办：  
   如果出错, 请添加 debug log：

```bash
acme.sh --issue ..... --debug 
```

或者：

```bash
acme.sh --issue ..... --debug 2
```

查看证书列表

```bash
acme.sh --list  
```

删除证书

acme.sh remove Main Domain(证书的主域名，上述证书列表中可看见)

8.注意事项：  
1、开启后请把所有网站的链接替换为https，尤其是图片链接等。推荐写链接时用//www.test.com而不是https://www.test.com，这种写法会优先使用HTTPS而且不会禁止HTTP。  
2、记得打开443端口。  
3、如果过了一段时间出现了类似NET :: ERR\_CERT\_AUTHORITY\_INVALID的错误，请检查是不是设置了证书链SSLCertificateChainFile。  
4、安装证书时，--key-file和--fullchain-file的参数是你想要把证书安装在的位置，而不是之前申请到的证书的位置。这个位置会在配置nginx时使用到。  
5、如果配置参数出错，最好只安装不要再申请。因为申请次数有限制。同一域名，每周最多申请10个证书，每周刷新。  
6、域名要写常用的。如果要使用https://www.test.com访问网页，域名选项-d 的参数一定要写www.test.com，如果申请证书和访问的域名不完全一致，访问时会提示不安全“访问的网站使用的安全证书域名错误”。

[fig1]: https://img2018.cnblogs.com/blog/867078/201903/867078-20190326175923357-720763416.png
[fig2]: https://common.cnblogs.com/images/copycode.gif
[fig3]: https://common.cnblogs.com/images/copycode.gif
[fig4]: https://common.cnblogs.com/images/copycode.gif

[https://github.com/Neilpang/acme.sh]: https://github.com/Neilpang/acme.sh

## reference

[用acme.sh帮你免费且自动更新的HTTPS证书，省时又省力](https://zhuanlan.zhihu.com/p/347064501)
