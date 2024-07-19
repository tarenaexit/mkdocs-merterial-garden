---
title: screego & 搭建局域网 https
number: 29
slug: discussions-29/
url: https://github.com/tarenaexit/mkdocs-merterial-garden/discussions/29
date: 2024-07-06
authors: [tarenaexit]
categories: 
  - 1.3-运维
labels: ['1.3.2-工具']
---

[搭建局域网 https](https://sanyers.github.io/blog/web/webrtc/%E6%90%AD%E5%BB%BA%E5%B1%80%E5%9F%9F%E7%BD%91https.html)
  

screego\[1\] 是一个由 Golang 开发的屏幕共享工具，我实际测试下来发现显示效果非常好，和大家分享下。

  

**_1\. 安装_**

  

screego 目前最新的版本为 v1.07，选择并下载系统对应的安装包：

```
[root@localhost ~]# wget https://github.com/screego/server/releases/download/v1.0.7/screego_1.0.7_linux_amd64.tar.gz
```

解压后可以得到二进制文件以及示例文件 screego.config.example，将文件重命名为 screego.config。目前目录文件如下：

```
screego-demo
├── LICENSE
├── README.md
├── screego
└── screego.config
```

  

**_2\. 配置_**

  

出于安全考虑，screego 会要求以 HTTPS 协议进行访问，所以在修改配置前，需要先生成下证书。

**_2.1 生成 HTTPS 证书_**

  

执行以下命令生成密钥 server.key，过程中会要求设置密码，按提示输入即可。

```
[root@localhost screego-demo]# openssl genrsa -des3 -out server.key 2048
```

接下来执行以下命令去除刚刚设置的密码：

```
[root@localhost screego-demo]# openssl rsa -in server.key -out server.key
```

为什么要去除密码呢？我测试过配置带有密码的密钥，结果服务无法正常启动，提示如下：

```
FTL http server error="tls: failed to parse private key"
```

使用密钥创建服务器证书的申请文件 server.csr，过程中会要求输入一些信息，不填也可。

```
[root@localhost screego-demo]# openssl req -new -key server.key -out server.csr
```

创建 CA 证书 ca.crt:

```
[root@localhost screego-demo]# openssl req -new -x509 -key server.key -out ca.crt -days 3650
```

创建服务器证书 server.crt:

```
[root@localhost screego-demo]# openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey server.key -CAcreateserial -out server.crt
```

目前目录文件如下：

```
screego-demo
├── ca.crt
├── ca.srl
├── LICENSE
├── README.md
├── screego
├── screego.config
├── server.crt
├── server.csr
└── server.key
```

密钥 server.key 和服务器证书 server.crt 已经创建，接下来就可以修改配置了。

  

**_2.2 修改配置_**

  

编辑配置文件 screego.config，这里仅列出我修改的配置项。

```
SCREEGO_EXTERNAL_IP=192.168.128.128
SCREEGO_SERVER_TLS=true
SCREEGO_TLS_CERT_FILE=/root/screego-demo/server.crt
SCREEGO_TLS_KEY_FILE=/root/screego-demo/server.key
```

说明：

> * SCREEGO\_EXTERNAL\_IP：访问地址，配置服务器的 IP 地址，以实际为准。
> 
> * SCREEGO\_SERVER\_TLS：TLS 开关。由于之前已配置了 HTTPS 的证书，这里改为 true。
> 
> * SCREEGO\_TLS\_CERT\_FILE：指定证书。
> 
> * SCREEGO\_TLS\_KEY\_FILE：指定密钥。

修改以上配置项后，服务就可以启动了。如果需要了解更多细节，可以查阅官方文档\[2\] 获取帮助。

  

**_3.启动_**

  

运行以下命令启动 screego：

```
[root@localhost screego-demo]# ./screego serve
```

没有报错的话，访问 https://192.168.128.128:5050 就可以看到建房页面了，如下图所示。这里的 IP 是我虚拟机的地址，大家以自己实际配置的为准。

![screego 安装配置教程：一款简单易用的屏幕共享工具](https://cdn.ccsyue.com/picx-images-hosting/master/2024/07/image.7p3hckit4s.webp "screego 安装配置教程：一款简单易用的屏幕共享工具")

点击 CREATE ROOM 按钮创建房间，再点击 Start Presentation，其他人通过访问相同的 URL 就可以看到共享的屏幕了。

![screego 安装配置教程：一款简单易用的屏幕共享工具](https://cdn.ccsyue.com/picx-images-hosting/master/2024/07/image.3k7w0go1aq.webp "screego 安装配置教程：一款简单易用的屏幕共享工具")

**_4\. 总结_**

  

\+ 开源的多用户屏幕共享工具，安装方便，使用简单

\+ 实测效果不错，屏幕显示清晰，无卡顿延迟现象

\+ 安全性

– 暂不支持快捷键操作

### References

`[1]``  `
_**screego: https://github.com/screego/server**_

`[2]`_*官方文档*__:_ _https://screego.net/#/_

  

  

> 原文始发于微信公众号（阿拉平平）：[screego 安装配置教程：一款简单易用的屏幕共享工具](http://mp.weixin.qq.com/s/kTAnZaS0omDJuNNoMclmpg)

<script src="https://giscus.app/client.js"
	data-repo="tarenaexit/mkdocs-merterial-garden"
	data-repo-id="RR_kgDOL4wNPw"
	data-mapping="number"
	data-term="29"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
