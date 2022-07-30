## 项目简介

在本项目中首先提取了python ecdsa库中的一部分对于ECDSA进行了实现，然后实现了泄露与重用随机数k等对ECDSA的不当使用方式、伪造合法签名造成的安全威胁。

## 代码说明

![image-20220731013400953](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310134593.png)

首先是对于ECDSA进行了实现，实现方法基本引用了openssl中的ECDSA，但还是做出了一定修改。

![image-20220731015642445](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310156369.png)

![image-20220731015659154](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310157513.png)

而后则是对于不同的不当使用方式进行模拟。

![image-20220731015714976](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310157270.png)

最后则是对于几种不同的方式进行了实现

## 运行指导

直接运行即可

## 运行结果

![image-20220731015739524](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310157037.png)

可以看到成功对于每一种方式成功进行了对应的攻击。