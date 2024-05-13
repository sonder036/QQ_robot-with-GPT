参考项目 [QChatGPT](https://github.com/RockChinQ/QChatGPT)， [mirai(本文部署的消息平台)](https://github.com/mamoe/mirai) 

chatgpt的API获取可以看[这个项目](https://github.com/chatanywhere/GPT_API_free)

## 前期准备

- 一个云服务器(本教程以阿里云服务器ECS为例，系统为	Ubuntu 22.04 64位)
- 一个QQ号（建议新注册一个号，该机器人会占用一个端的登录，而且很容易被冻结）
- 需要会一些简单的linux命令，以及了解文件编辑工具如`vim`等。

## 如何部署

作者使用[XSHELL](https://www.xshell.com/zh/xshell/)和[XFTP](https://www.xshell.com/zh/xftp/)进行远程控制云服务器和文件管理，两个软件上手都比较容易。

### 首先找到公网IP

- 在云服务器控制台找:

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/c287d095-1a08-4818-87c2-447db2434e05)

- 在控制台输入`curl cip.cc`:
  
 ![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/b6ccec3f-8384-4c49-8d9d-96b4d0841ca2)


### XSHELL连接

下载好后先点击左上角的新建，然后如下图所示：

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/b24a3a96-3c56-4cb8-930f-73232138139f)

为了之后连接服务器更加方便可以在`登陆提示符`选项中填入你的用户名和密码。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/77d91103-1ab3-491f-9088-d61130fccec7)

`XFTP`连接方式与 `XSHELL` 相似，这里不再赘述。

于是乎，即使你不太擅长linux的下载和文件操作也能跟着[QChatGPT部署教程](https://qchatgpt.rockchin.top/posts/deploy/qchatgpt/manual.html)进行，不过要注意不要下载成windows系统的文件。

### 安装主程序

- 克隆项目

在服务器终端输入

```
//新建个文件夹放项目
mkdir QQ_robot
//进入文件夹
cd QQ_robot
//克隆仓库
git clone https://github.com/RockChinQ/QChatGPT
//克隆完后目录下会多一个名为QchatGPT的文件夹，此时进入文件夹
cd QchatGPT
```

2.安装依赖

```
pip3 install -r requirements.txt
```

3.运行主程序

```
python3 main.py
```

此时显示如下图即为安装完成：

![运行GchatGPT主程序](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/e5f82e62-705e-4e5f-8a10-771d92c8dd63)

### 部署mirai信息平台

```
//退出QchatGPT文件夹
cd ..
//新建文件夹mirir
mkdir mirai
```

可以输入 `ls` 查看当前目录下的文件

![ls效果](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/0dcea798-fd7c-4d52-8aef-546223792c1e)


进入 `mirai` 文件夹

```
cd mirai
```

安装 `mirai-console`

```
//利用wget指令下载
wget https://github.com/iTXTech/mcl-installer/releases/download/v1.0.7/mcl-installer-1.0.7-linux-amd64-musl
//当然你也可以在你的主机上下载，再通过XFTP传到服务器相应位置
```
此时为下载完成
![下载完成效果](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/edffcc65-e5df-46b3-a3eb-8edee195c44c)

```
//给文件执行权限
chmod +x mcl-installer-1.0.7-linux-amd64-musl
//运行安装文件
./mcl-installer-1.0.7-linux-amd64-musl
```

此时出现如下效果，一路按回车键即可完成安装

![安装mirai-console](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/f81c45c2-ca06-4bf6-98af-9192b786b864)

安装完成后,输入ls应为如下界面

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/485e059a-3782-44b7-8f83-a88aefa7d066)

之后给 `mcl` 文件执行权限并运行

```
chmod +x mcl
./mcl
//之后一路回车就行
```

到如下界面时，输入 `mcl --update-package net.mamoe:mirai-api-http --channel stable-v2 --type plugin` ，回车，完成后显示新的 `>` 时，可以按 `Ctrl+C` 退出mcl。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/c1adfca0-0c9d-4b82-9360-37043a198b94)

再次进入 `mcl` ，他会下载一些文件，完成后按 `Ctrl+C` 退出即可。

转入配置文件夹，修改 `setting.yml` 文件

```
cd ./config/net.mamoe.mirai-api-http/
vim setting.yml
//如果你没有下载vim可以输入apt install vim 进行下载
```

进入 `vim` 界面后，按下 `10dd` (vim删除指令，dd前面是几就删几行) 删除原来的文本,将下面的代码复制上去，`vim`可以按 `p` 进行粘贴，你也可以直接鼠标右键粘贴到终端。

之后按 `:wq` 保存并退出即可。

> ps: 如果不会用vim可以上网查一些教程，很多熟悉的快捷键在vim上无法使用，也可能误入到其他地方，遇到这种情况建议直接bing查一下。

```yml
adapters:
  - ws
debug: true
enableVerify: true
verifyKey: yirimirai
singleMode: false
cacheSize: 4096
adapterSettings:
  ws:
    host: localhost
    port: 8080
    reservedSyncId: -1

```

更改完成后输入 `cd ../..` 退出的到 `mirai` 目录下，此时再打开 `mcl` 文件，等他再度初始化完成后退出即可。

### 配置签名服务

这一部分涉及文件操作比较麻烦，可以在主机上完成，通过 `XFTP` 传文件

[点击这里](https://github.com/MrXiaoM/qsign/releases/download/1.2.0-final/qsign-1.2.1-beta-dev-d62ddce-all.zip)qsign一键签名包，下载完成后全部解压缩，将里面的两个文件夹复制到 `marai` 文件夹中。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/b1d649ef-8c1a-4cbd-af5d-5aa7970d2fa9)

再度打开 `mcl` 文件，等待初始化完成后退出。

之后打开 `marai/config/top.mrxiaom.qsign` 下的 'config.yml' 文件

```
cd ./config/top.mrxiaom.qsign/
vim config.yml
```

按一下 `i` 进入编辑模式 然后把 `base-path` 参数改成  'txlib/8.9.90' 

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/24642a00-1e19-4a81-a2f1-72453a0506a2)

之后按 `Esc` + `:wq` 保存并退出。

### 运行marai

-------------
施工ing
