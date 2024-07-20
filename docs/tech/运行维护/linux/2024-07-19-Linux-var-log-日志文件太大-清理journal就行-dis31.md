---
title: Linux /var/log/日志文件太大，清理journal就行
number: 31
slug: discussions-31/
url: https://github.com/tarenaexit/mkdocs-merterial-garden/discussions/31
date: 2024-07-19
authors: [tarenaexit]
categories: 
  - 1.3-运维
labels: ['1.3.3-linux']
---

[Linux /var/log/日志文件太大，清理journal就行](https://www.uedbox.com/post/58901/)
在[CentOS](https://www.uedbox.com/post/tag/centos/ "CentOS") 7开始使用的`systemd`使用了`journal`日志，这个日志的管理方式和以往使用syslog的方式不同，可以通过管理工具维护。

### Linux log日志占用

[Linux](https://www.uedbox.com/post/tag/linux/ "Linux")使用`df -h`检查磁盘文件，可以看到`/run`目录下有日志目录`/run/log/journal`，占用了数G空间。

或者直接在相应目录下执行`du --max-depth=1 -h`


```
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/centos-root  8.5G  4.2G  4.4G  49% /
tmpfs                     16G  1.6G   15G  11% /run

[rss@VM_0_16_centos log]# du --max-depth=1 -h
254M    ./php-fpm
36K     ./anaconda
256K    ./redis
4.0K    ./chrony
4.0K    ./ppp
4.0K    ./ntpstats
256K    ./letsencrypt
4.0G    ./journal
34M     ./audit
24K     ./tuned
4.6G    .
```


在日志目录下有很多历史累积的日志。

### Linux log日志清理

检查当前journal使用磁盘量


```
journalctl --disk-usage
```


清理方法可以采用按照日期清理，或者按照允许保留的容量清理，只保存2天的日志，最大500M


```
journalctl --vacuum-time=2d
journalctl --vacuum-size=500M
```


如果要手工删除日志文件，则在删除前需要先轮转一次journal日志


```
systemctl kill --kill-who=main --signal=SIGUSR2 systemd-journald.service
```


要启用日志限制持久化配置，可以修改 `/etc/systemd/journald.conf`


```
SystemMaxUse=16M
ForwardToSyslog=no
```


然后重启


```
systemctl restart systemd-journald.service
```


检查journal是否运行正常以及日志文件是否完整无损坏


```
systemctl restart systemd-journald.service
```


<script src="https://giscus.app/client.js"
	data-repo="tarenaexit/mkdocs-merterial-garden"
	data-repo-id="RR_kgDOL4wNPw"
	data-mapping="number"
	data-term="31"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
