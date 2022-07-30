## 项目简介

在这个project中使用了 SM3 实现中的加密函数，模拟了对于 SM3 的长度扩展攻击。即通过已知的 SM3(m_1) 的值，计算得出 $SM3(m_1||1||0...0||lengh_{m_1}||m_2)$ 的值。

但是在实际中，服务器在进行加密的过程之前会添加一个保密的 secret 在消息前，实际上加密的内容为 SM3(secret||m_1) 。但长度扩展攻击的方法仍然一致，只是需要得到 secret 的长度，具体的，可以通过遍历的方法尝试后得到。在这次实现中，通过利用可以多次询问服务器得到签名值的方式，遍历得到了 secret 的长度。在得到了secret 的长度后就可以利用长度扩展攻击函数对于任意的消息 $m_1,m_2$  进行长度扩展攻击。

## 代码说明

![image-20220731010943871](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310109900.png)

![image-20220731011001573](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310110502.png)

首先是SM3的加密

![image-20220731011034825](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310110265.png)

而后是对于sm3的长度扩展攻击

![image-20220731011100094](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310111969.png)

接下来是对于盐值的长度的查找，模拟实际中服务器会在消息前添加盐值的情况，需要使用遍历的方法找出盐值的长度。具体的，可以对于盐值的长度进行猜测，然后直接进行长度扩展攻击，如果猜对长度，那么攻击将成功。可以因此得到盐值的长度。

![image-20220731012056992](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310120211.png)

最后对于长度扩展攻击进行测试，实现了长度扩展攻击，并且与实际扩展后的哈希值进行了对比。

## 运行指导

直接运行即可，注意所输入的十六进制串中字母都应大写。

## 运行结果

![image-20220731012615436](https://cdn.jsdelivr.net/gh/fffffishhhhh/picture/202207310126421.png)

可以看到成功对于盐值的长度进行了猜测，并且成功进行了攻击
