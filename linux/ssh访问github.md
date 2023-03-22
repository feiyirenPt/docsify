# ssh访问github

## 问题
```bash
error ssh: connect to host github.com port 22: Connection timed out
```

## 解决方案

```conf
Host github.com
User 注册github的邮箱
Hostname ssh.github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
Port 443
```
[参考文章](https://blog.csdn.net/nightwishh/article/details/99647545)
