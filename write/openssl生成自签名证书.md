---
title: openssl生成自签名证书
date: 2023-02-25 10:04  
tags: [openssl]  
source: https://www.jianshu.com/p/0e9ee7ed6c1d  
---
## openssl生成自签名证书

**下面生成的证书是用来网站启用https用的**

*有点麻烦，要自己建一个CA，然后对自己的请求文件进行认证然后生成证书，私钥和证书，一共俩*

ubuntu上一般都自带安装了OpenSSL

```bash
ubuntu:~$ openssl
OpenSSL> version
OpenSSL 1.1.1  11 Sep 2018
OpenSSL>
```

#### 基本概念


-   ***CA***：认证机构。有自己的**证书**，可以拿自己的证书给别人签名然后收钱，这个星球上的CA被几家说英语的人垄断了。在这里我们会虚拟出一个CA机构，然后用他来给自己的证书认证签名。
-   ***(网站)证书*** ：发送给客户端的证书，其中大部分是公钥。是一个包含自己网站的公钥、认证、签名等信息的文件。
-   ***(网站)私钥*** ：服务器留存的解密私钥(server)

*注意区分 **CA机构的证书**（可以拿来给其他网站证书签名）和 **自己网站的证书**（不可以），不一样*

- 常用后缀名

| 格式 | 说明 |
| --- | --- |
| `.crt` `.cer` | 证书(Certificate) |
| `.key` | 密钥/私钥(Private Key) |
| `.csr` | 证书认证签名请求(Certificate signing request) |
| `*.pem` | base64编码文本储存格式，可以单独放证书或密钥，也可以同时放两个；**base64编码**就是两条-------之间的那些莫名其妙的字符 |
| `*.der` | 证书的二进制储存格式(不常用) |

#### 基本流程

1.  搞一个虚拟的CA机构，生成一个证书
2.  生成一个自己的密钥，然后填写证书认证申请，拿给上面的CA机构去签名
3.  于是就得到了**自（自建CA机构认证的）签名证书**

### 首先，虚构一个CA认证机构出来

```bash
# 生成CA认证机构的证书密钥key
# 需要设置密码，输入两次
openssl> genrsa -des3 -out ca.key 1024

# 去除密钥里的密码(可选)
# 这里需要再输入一次原来设的密码
openssl> rsa -in ca.key -out ca.key

# 用私钥ca.key生成CA认证机构的证书ca.crt
# 其实就是相当于用私钥生成公钥，再把公钥包装成证书
openssl> req -config openssl.cnf -new -x509 -key ca.key -out ca.crt -days 365
# 这个证书ca.crt有的又称为"根证书",因为可以用来认证其他证书
```

### 其次，才是生成网站的证书

*用上面那个虚构出来的CA机构来认证，不收钱！*

```bash
# 生成自己网站的密钥server.key
openssl> genrsa -des3 -out server.key 1024

# 生成自己网站证书的请求文件
# 如果找外面的CA机构认证，也是发个请求文件给他们
# 这个私钥就包含在请求文件中了，认证机构要用它来生成网站的公钥，然后包装成一个证书
openssl> req -config openssl.cnf -new -key server.key -out server.csr
# 移除密码
openssl> rsa -in server.key -out server.key

# 使用虚拟的CA认证机构的证书ca.crt，来对自己网站的证书请求文件server.csr进行处理，生成签名后的证书server.crt
# 注意设置序列号和有效期（一般都设1年）
openssl> x509 -req -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out server.crt -days 365
```

至此，私钥`server.key`和证书`server.crt`已全部生成完毕，可以放到网站源代码中去用了。

___

*以下是闲话：*

### 后缀名与文件内容

*其实后缀名不影响文件的实质内容的，内容都可以文本打开看，囧*

-   例如生成的`ca.key`文件，输入两次密码，然后再查看其内容：

```bash
OpenSSL> genrsa -des3 -out ca.key 1024
Generating RSA private key, 1024 bit long modulus (2 primes)
....+++++
...........................................................................+++++
e is 65537 (0x010001)
Enter pass phrase for ca.key:
Verifying - Enter pass phrase for ca.key:
OpenSSL> exit
ubuntu:~/web/ssl$ ls
ca.key
ubuntu:~/web/ssl$ cat ca.key
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,6D519E92415BEE33

UcZyq1NkoodzdWBHq37G2+y+Q/QigaPmXdNjZA7rBbz17VVqB1JrU11tbFo5BDZV
...
-----END RSA PRIVATE KEY-----
ubuntu:~/web/ssl$
```

-   再如生成`ca.crt`证书文件：

```bash
OpenSSL> req -new -x509 -key ca.key -out ca.crt -days 365
Can't load /home/xqq/.rnd into RNG
139920876560832:error:2406F079:random number generator:RAND_load_file:Cannot open file:../crypto/rand/randfile.c:88:Filename=/home/xqq/.rnd
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:cn
State or Province Name (full name) [Some-State]:spn
Locality Name (eg, city) []:ln
Organization Name (eg, company) [Internet Widgits Pty Ltd]:on
Organizational Unit Name (eg, section) []:oun
Common Name (e.g. server FQDN or YOUR name) []:cn
Email Address []:ea
OpenSSL> exit

ubuntu:~/web/ssl$ ls
ca.key ca.crt ca.lol  # ca.lol是我自己乱起的扩展名

# ca.lol
ubuntu:~/web/ssl$ cat ca.lol
-----BEGIN CERTIFICATE-----
MIICqjCCAhOgAwIBAgIUAOsXW5KDRNvBDTLaIreadCJVnn4wDQYJKoZIhvcNAQEL
...
-----END CERTIFICATE-----

# ca.key
xqq@VM-0-4-ubuntu:~/web/ssl$ cat ca.key
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQCxImyGkSj2rB7zSNSM/2h4dg5tpJNGwJDQLE/PNKQtkorMgrbI
...
-----END RSA PRIVATE KEY-----
xqq@VM-0-4-ubuntu:~/web/ssl$
```

> 看嘛，扩展名并不影响密钥文件的内容
