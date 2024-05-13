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

- 安装依赖

```
pip3 install -r requirements.txt
```

- 运行主程序

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

[点击这里](https://github.com/MrXiaoM/qsign/releases/download/1.2.0-final/qsign-1.2.1-beta-dev-d62ddce-all.zip)qsign一键签名包，下载完成后全部解压缩，将里面的两个文件夹复制到 `mirai` 文件夹中。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/b1d649ef-8c1a-4cbd-af5d-5aa7970d2fa9)

再度打开 `mcl` 文件，等待初始化完成后退出。

之后打开 `mirai/config/top.mrxiaom.qsign` 下的 'config.yml' 文件

```
cd ./config/top.mrxiaom.qsign/
vim config.yml
```

按一下 `i` 进入编辑模式 然后把 `base-path` 参数改成  `txlib/8.9.90` 

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/24642a00-1e19-4a81-a2f1-72453a0506a2)

之后按 `Esc` + `:wq` 保存并退出。

### 运行mirai

退回至 `mirai` 目录，运行 `mcl` 文件。初始化完成后输入:

```
login [你的QQ账号] [你的qq密码]
```

出现以下界面后，复制连接到浏览器，按 `F12` 查看源码。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/98cb7427-982b-48f9-8871-57f47da0d1f3)

此处用 `edge` 浏览器为例，`Chrome` 同理，点击 `网络` 后刷新一下，会出现一下效果：

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/c37dcb13-88fc-43e8-b76e-05efa200adb1)

之后完成登录验证，`名称` 栏目会出现 `cap_union_new_verify` 点开后点击预览，之后复制 `ticket` 到服务器终端（注意要复制ticket引号内所有内容，很长记得复制全）。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/41bf82b4-c889-40c5-bd77-5cd5cf7a8802)

之后会要短信验证码什么的，按指引来就行，出现下图情况即为登陆成功。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/11c61ac7-1a52-4872-b8f5-6a6928e8b08d)

之后按 `Ctrl+C` 退出即可。

### 填写配置信息

先转到 `QchatGPT` 目录下，进入 `data/config/` 文件夹

```
//假设你在mirai目录下，如果不在的话可以借助ls指令用cd转到QcharGPT目录下
cd ..
cd ./QchatQPT
cd ./data/config
```

#### 配置platform.json

```
//用vim编辑platfrom.json
vim platfrom.json
```

点 `i`进入Insert模式，修改一下参数，然后`ESC`+`:wq`退出：

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/65999f96-deb4-49b2-9ceb-ce7d440440ec)

#### 配置provider.json

```
//用vim编辑provider.json
vim provider.json
```
在主机点击[这个连接](https://github.com/chatanywhere/GPT_API_free)可以凭github账号获取一个免费的 API，然后在服务器中的 `provider.json` 做以下修改，之后保存并推出即可：

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/9217bed6-eb90-4d11-9306-1c4dd77b0b2c)

以上就完成了文件的配置，下面我们将在服务器上保持机器人24h运行。

### 利用screen挂起机器人

#### screen简介

使用`screen`可以实现以下功能:

- 会话恢复：只要Screen本身没有终止，在其内部运行的会话都可以恢复。这一点对于远程登录的用户特别有用——即使网络连接中断，用户也不会失去对已经打开的命令行会话的控制。只要再次登录到主机上执行screen -r就可以恢复会话的运行。同样在暂时离开的时候，也可以执行分离命令detach，在保证里面的程序正常运行的情况下让Screen挂起（切换到后台）。
- 多窗口：在Screen环境下，所有的会话都独立的运行，并拥有各自的编号、输入、输出和窗口缓存。用户可以通过快捷键在不同的窗口下切换，并可以自由的重定向各个窗口的输入和输出。
- 会话共享：Screen可以让一个或多个用户从不同终端多次登录一个会话，并共享会话的所有特性（比如可以看到完全相同的输出）。它同时提供了窗口访问权限的机制，可以对窗口进行密码保护。

以上摘自知乎[这篇文章](https://zhuanlan.zhihu.com/p/405968623)，可以看一下了解 `screen` 指令。

#### 下载screen

```
// 终端输入以下指令安装screen
apt install screen
// 查看 screen 版本，正常显示则说明安装完成
screen -v 
```

#### 利用sreen挂起机器人

```
//创建一个名为QQBOT的虚拟终端，输入后即进入终端
screen -S QQBOT
```

之后转入 `miria` 目录，执行 `mcl`，初始化完成后用上文所述的`login`指令登录QQ。

登陆成功后用 `Ctrl+A+C` 在该终端下新建一个窗口，此时你可以使用以下指令切换窗口：
```
//转到下一个窗口
Ctrl+A+P
//返回上一个窗口
Ctrl+A+N
```

当然，现在是不用转换的，你只需要在新的窗口下进入 `QchatGPT` 目录运行 `main.py` 即可。


![连接到QQ账号](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/dac73da8-69ec-4a4f-9e9c-573384cf6142)

如上图，显示成功登陆到账号，则QQ机器人成功运行，可以在群聊里 @机器人 或者私聊。

![image](https://github.com/sonder036/QQ_robot-with-GPT/assets/59356759/2bdfa2bf-f8ed-40d8-96bb-628e1e71ba7f)

确定QQ机器人正常运行后，可以先按 `Ctrl+A` 再按 `Ctrl+D` 退回到终端，如果你以后要重新进入`screen`,可使用以下指令：

```
// 查看存在的screen终端列表
screen -ls
// 看到终端id后，输入以下指令，即可进入虚拟终端
screen -r [你的终端id]
```

### 机器人扩展

可以查看文章最开头给出的参考项目下载插件。

> 码字不易，如果有帮助可以给个star
> 
> 祝工作顺利，学业有成
