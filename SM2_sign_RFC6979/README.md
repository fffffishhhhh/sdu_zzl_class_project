## 项目简介

在该项目中，以python库 gmssl为基础，利用RFC6979代替了SM2签名时所使用的生成随机数部分，并且通过改变过后的库实现了SM2的签名以及验证过程。

## 代码说明

代码首先对于gmssl库进行了一部分修改，利用利用RFC6979代替了SM2签名时所使用的生成随机数部分

![image-20220731002944317](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310029489.png)

然后使用改动过后的库对于sm2进行了实现

![image-20220731003041167](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310030121.png)

首先是签名以及验证函数

![image-20220731003059401](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310031442.png)

![image-20220731003113102](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310031983.png)

而后是一些在生成密钥以及运算时所需要的椭圆曲线上的操作函数

![image-20220731003155610](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310031062.png)

以及密钥生成函数和数据预处理的函数

![image-20220731003219486](C:/Users/ASUS/AppData/Roaming/Typora/typora-user-images/image-20220731003219486.png)

最后对于以上内容进行了测试

## 运行指导

直接运行即可

## 运行结果

![image-20220731003332871](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310033338.png)

可以看到以上内容成功生成了公私钥对，并且对于消息进行了签名，而后成功验证。