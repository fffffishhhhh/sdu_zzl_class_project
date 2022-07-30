## 项目简介

本项目中实现了，通过已知签名恢复公钥，并且利用恢复出的公钥对于签名进行伪造，并且成功通过验证。

## 代码说明

本实验中采用的ECDSA是在openssl中的ECDSA库进行了一点修改后的。

![image-20220730221845652](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302219366.png)

首先初始化函数，确定椭圆曲线类型

![image-20220730222620113](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302226471.png)

![image-20220730222833271](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302228673.png)

接下来定义签名与验证的函数，其中weak verify的验证是直接根据消息的哈希值进行验证。

![image-20220730222950498](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302229721.png)

接下来利用已知签名恢复公钥，并且进行验证，再使用已知公钥对于签名进行伪造

![image-20220730223403705](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302234297.png)

最后进行测试

## 运行指导

直接运行即可

## 运行结果

![image-20220730223546168](C:/Users/ASUS/AppData/Roaming/Typora/typora-user-images/image-20220730223546168.png)

可以看到成功对于公钥进行了恢复，并且成功进行了伪造