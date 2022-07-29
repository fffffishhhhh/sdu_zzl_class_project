## 项目简介

在该项目中，利用SM2对于PGP进行了实现，由于在实现过程中搭建一个实际的邮箱服务器过于复杂，所以仅仅是对于加密解密函数进行了实现，而简化了实际的数据传输环节。

## 代码说明

![image-20220730012638358](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20220730012638358.png)

本代码通过对于gmssl库中的sm2函数进行了一点修改并存在了sm2.py中，在实现pgp的时候对于该文件进行了调用。

![image-20220730012840025](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20220730012840025.png)

这一部分对于一些数学工具进行了实现。

![image-20220730013019981](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20220730013019981.png)

而后实现了公钥对的生成与记录，以及数据的处理函数

![image-20220730013153043](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20220730013153043.png)

最后是PGP相关的函数。

![image-20220730013212057](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20220730013212057.png)

最后测试中假设发送方发送了 'this is a test mail' 接收者收到并进行解密。

## 运行指导

直接运行即可

## 运行结果

![image-20220730013413816](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20220730013413816.png)

可以看到接收者成功对于收到的邮件进行了解密