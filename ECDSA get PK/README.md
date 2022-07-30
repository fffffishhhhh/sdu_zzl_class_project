## 项目简介

在本实验中对于ECDSA中通过已知签名恢复公钥的算法的原理进行了描述，并且进行了实现。其中原理写在了pdf文件中。

## 代码说明



![image-20220730225935572](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302259710.png)

![image-20220730225954926](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302259844.png)

![image-20220730230015082](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302300507.png)

代码与ECDSA forge sign中的类似，仅仅是取消掉了伪造签名的部分。

## 运行指导

直接运行即可

## 运行结果

![image-20220730232557086](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207302326792.png)

可以看到成功对于公钥进行了恢复