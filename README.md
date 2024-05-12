参考项目 [QChatGPT](https://github.com/RockChinQ/QChatGPT)， [mirai](https://github.com/mamoe/mirai) 

chatgpt的API获取可以看[这个项目](https://github.com/chatanywhere/GPT_API_free)

## 前期准备

- 一个云服务器(本教程以阿里云服务器ECS为例，系统为	Ubuntu 22.04 64位)

## 如何部署

在 [QChatGPT部署教程](https://qchatgpt.rockchin.top/posts/deploy/qchatgpt/manual.html)中有在windows本地环境中部署QQ机器人的详细教程此处不再赘述，主要提出在linux与服务器下部分操作的差异。

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

