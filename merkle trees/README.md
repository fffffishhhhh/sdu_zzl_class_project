## 项目简介

本项目中使用 python 实现了 Merkle Tree 数据结构，并创建了一个拥有 10 万个叶子结点的 Merkle Tree。对于随机选择的一个结点，我们可以根据给出 的 hash 值，验证其是否存在于 Merkle Tree 中。并且对于一个示例进行了简单的验证。

## 代码说明

![image-20220731002132203](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310021103.png)

首先对于树进行建立，创建类并且添加相应的库函数

![image-20220731002240233](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310022518.png)

接下来是证明链的完成以及对于树的遍历

![image-20220731002326885](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310023831.png)

最后我们对于该树进行测试，建立树并且进行存在性证明

## 运行指导

直接运行即可

## 运行结果

![image-20220731002451856](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310024698.png)

可以看到成功建立了树并且对于节点成功进行验证