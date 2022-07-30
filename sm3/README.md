## 项目简介

在该项目中，对于 SM3 加密算法进行了实现。实现过后与已知库代码进行了验证，可以得到算法的输出与调用库的输出一致（由于本项目对于‘abc’认为是一个16进制数，所以与gmssl给出的示例（将‘abc’转换成了ASCII码）结果不同）。在提交的版本中并没有包含测试的内容。

## 代码说明

![image-20220731003827541](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310038733.png)

首先对于一些需要的变量进行定义

![image-20220731003912931](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310039994.png)

接下来定义一些基本的操作函数、

![image-20220731003956551](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310039760.png)

而后定义消息填充函数

![image-20220731004032053](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310040759.png)

消息扩展

![image-20220731004057853](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310041669.png)

轮函数

![image-20220731004119606](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310041121.png)

最后是完整的加密函数

![image-20220731004136196](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310041196.png)

对于已完成的函数进行测试

## 运行指导

直接运行即可，注意所输入的十六进制串中字母都应大写。

## 运行结果

![image-20220731004219159](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310042044.png)

可以看到成功对于数据进行了加密