## 项目简介

在这个项目中实现了对于 sm3 的生日攻击，分别实现了两个版本

1. 最基本版本的实现，采用随机选取输入值，并且储存所有输入以及其对应的前n比特的值，当存在两个输入的前n比特值相同的时候输出。但是对于存储大小有着一定要求。
2. rho版本的实现，是一个空间复杂度为 O(1)的方式，采用了类似快慢指针的思想，成功对于碰撞进行查找，并且与传统的生日攻击攻击成功的概率相同。

## 代码说明

![image-20220731005532438](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310055319.png)

![image-20220731005551572](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310055420.png)

首先是对于SM3的实现

![image-20220731005733942](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310057429.png)

而后定义函数生成随机数作为碰撞的输入

![image-20220731005758816](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310057771.png)

接下来是普通版本的生日攻击，对于查表的部分，通过建立一个数组，将哈希值作为索引值，数组内容为原象的值，当对应的哈希值的位置不为空时，就相当于找到了碰撞。

![image-20220731005930938](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310059400.png)

而后是rho算法

![image-20220731010232980](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310102359.png)

最后以碰撞20位为例，对于两种方法进行测试

## 运行指导

直接运行即可，注意所输入的十六进制串中字母都应大写。

## 运行结果

![image-20220731010729500](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310107514.png)

可以看到两种方法均能碰撞出20比特，并且运行出的结果可以成功通过验证