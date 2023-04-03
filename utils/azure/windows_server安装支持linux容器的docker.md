---
title: indows server上安装支持linux容器的docker  
date: 2023-01-11 23:35  
tags: [ azure,windows server,v2ray ]  
source: https://www.cnblogs.com/smallidea/p/16307782.html
---
## 需求：

有一台 azure windows server core2022,想部署v2ray实现代理上网

## 问题：

选择用docker部署v2ray,但是docker起不来

## 安装过程：

###  安装 docker

#### 安装hyper-v
[参考链接][lk1]

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

```cmd
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```
####  安装支持linux的 docker

需要安装 Docker Enterprise Edition Preview，这个版本内部包含了一个 LinuxKit 系统用于运行 Docker Linux 容器.

```powershell
## 卸载 Docker CE.
Uninstall-Package -Name docker -ProviderName DockerMSFTProvider

## 如果你使用运行在Hyper-V上的Linux虚拟机运行Docker容器，启用嵌套虚拟化
Get-VM WinContainerHost | Set-VMProcessor -ExposeVirtualizationExtensions $true
```
---
 error:   
	* 所选规格不支持安装跑linux容器的docker,因为无法开启嵌套虚拟化  
	* 我的windows server是跑在`Standard B1s (1 vcpu，1 GiB 内存)`的,应该是不支持嵌套虚拟化的
	* windows容器docker倒是可以跑
---

```powershell
## 安装 docker preview
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
Install-Module DockerProvider
Install-Package Docker -ProviderName DockerProvider -RequiredVersion preview

## 允许 LinuxKit 系统运行linux 容器
[Environment]::SetEnvironmentVariable("LCOW_SUPPORTED", "1", "Machine")

## 如果有需要，可以切换回 支持windows容器
[Environment]::SetEnvironmentVariable("LCOW_SUPPORTED", "$null", "Machine")

## 重启docker服务
Restart-Service docker
```

## 测试
docker version
docker run -it --rm ubuntu /bin/bash


###  安装 docker-compose

建议使用如下脚本，一直在用没有什么问题

```powershell
Invoke-WebRequest -UseBasicParsing -Outfile $Env:ProgramFiles\docker\docker-compose.exe https://smartidedl.blob.core.chinacloudapi.cn/docker/compose/releases/download/1.29.2/docker-compose-Windows-x86_64.exe
```
## 尝试直接安装hyper-V,装个linux虚拟机,再装docker,最后再装v2ray
- 也是嵌套虚拟化不能解决

## 解决
最后直接用 `scoop install v2ray nginx`解决了

[lk1]: https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
