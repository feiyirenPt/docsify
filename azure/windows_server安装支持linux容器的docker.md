---
title: windows server 上安装支持linux容器的docker - 远方V3 - 博客园  
date: 2023-01-11 19:48  
tags: []  
source: https://www.cnblogs.com/smallidea/p/16307782.html
---
## 需求：

搭建了一个ads （azure devops server） ci/cd 流水线，会用到windows的代理机，这台机器需要安装docker，并可运行linux类型的container  
注：关于如何在windows上安装angent可以直接在ads上查看

## 问题：

这个机器系统是windows 10，重启后不登录docker无法运行起来，所以选择了在windows server 运行 docker，从而达到无需登录也可以使用的目的

## 安装过程：

### 2. 安装 docker

#### 2.1. 安装hyper-v
[参考链接][lk1]

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

```cmd
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```
#### 2.2. 安装支持linux的 docker

需要安装 Docker Enterprise Edition Preview，这个版本内部包含了一个 LinuxKit 系统用于运行 Docker Linux 容器.

```powershell
## 卸载 Docker CE.
Uninstall-Package -Name docker -ProviderName DockerMSFTProvider

## 如果你使用运行在Hyper-V上的Linux虚拟机运行Docker容器，启用嵌套虚拟化
Get-VM WinContainerHost | Set-VMProcessor -ExposeVirtualizationExtensions $true

## 安装 docker preview
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
Install-Module DockerProvider
Install-Package Docker -ProviderName DockerProvider -RequiredVersion preview

## 允许 LinuxKit 系统运行linux 容器
[Environment]::SetEnvironmentVariable("LCOW_SUPPORTED", "1", "Machine")

## 重启docker服务
Restart-Service docker
```

## 测试
docker version
docker run -it --rm ubuntu /bin/bash

## 如果有需要，可以切换回 支持windows容器
[Environment]::SetEnvironmentVariable("LCOW_SUPPORTED", "$null", "Machine")

### 2.3. 安装 docker-compose

建议使用如下脚本，一直在用没有什么问题

```powershell
Invoke-WebRequest -UseBasicParsing -Outfile $Env:ProgramFiles\docker\docker-compose.exe https://smartidedl.blob.core.chinacloudapi.cn/docker/compose/releases/download/1.29.2/docker-compose-Windows-x86_64.exe
```
[lk1]: https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
