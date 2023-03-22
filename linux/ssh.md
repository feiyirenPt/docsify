---
title: ssh  
date: 2022-10-11  
tags: ssh  
---
## ssh公钥上传服务器
- on server:
```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_key
```
- on client:
```bash
ssh-copy-id -i id_rsa.pub username@ip[:port]
```

## windows下ssh免密登录
服务端切换到`C:\\ProgramData\\ssh\\`下（首次启动sshd后会生成该文件夹），打开sshd_config文件，

修改文件（以下是重点）：

```bash
# 确保以下3条没有被注释
PubkeyAuthentication yes
AuthorizedKeysFile	.ssh/authorized_keys
PasswordAuthentication no

# 确保以下2条有注释掉 重点，这两行要注释
# Match Group administrators
# AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
```