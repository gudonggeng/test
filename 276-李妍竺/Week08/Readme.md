# keras

keras是由python编写的基于theano/tensorflow的深度学习框架

步骤：
1. 载入训练数据和检测数据（mnist）：手写数字数据库
2. 输出测试用的第一张图
3. **使用tensflow.Keras搭建一个有效识别图案的神经网络**
4. 数据归一化，并将数据标签转化为二进制
5. 训练模型
6. 输入测试数据
7. 测试效果

# 从零实现手写数字
## 神经网络训练过程：
1. 参数的随机初始化(权重)
```
0-1随机（-0.5~0.5）
self.wih = numpy.random.rand(self.hnodes, self.inodes) - 0.5  # random.rand:生成0-1的随机数  
self.who = numpy.random.rand(self.onodes, self.hnodes) - 0.5

高斯随机
self.wih = (numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes)))  
self.who = (numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes)))
```

2. 前向传播计算每个样本对应的输出节点激活函数值
     激活函数必须满足：**1.非线性 2.可微性 3.单调性**

  常用的激活函数：
    
    1.sigmoid函数:

$$y = logsig(x)= \frac{1}{1+e^{-x}} $$

    2.tanh函数
    
$$y = tansig(x) = \frac{e^x-e^{-x}}{e^x+e^{-x}}$$
    
    3.ReLU函数
$$f(x) = max(0,x) $$

    4.Softmax函数
$$S_{i}=\frac{e^{V_{i}}}{\sum_{j}e^{V_{j}}}$$

其中： Softmax函数用于多分类过程中，将多个神经元的输出，映射到[0,1]区间内，可以看成概率理解。
```
在special库中：
sigmod:scipy.special.expit(x)
```

3. 计算损失函数
     **损失函数：** 差值。
        1. 均值平方差（MSE）
         *一般输入实数、无界的值，用MSE*
$$MSE = \sum^n_{i=1}\frac{1}{n}(f(x_{i})-y_{i})$$
        2. 交叉熵（cross entropy）：值越小，结果越准。分类， 属于哪一类。
         *一般输入标签是位矢量（分类标签），使用交叉熵。*
$$C = -\frac{1}{n}\sum_{x}[y\ln a+(1-y)\ln(1-a)]$$

4. 反向传播计算偏导数
5. 使用梯度下降或者先进的优化方法更新权值
     **梯度下降法**
     梯度方向表示函数值增大的方向，梯度的模表示函数值增大的速率。
     *沿着梯度方向，反向更新，得到函数的最小值*。（全局最小值或局部最小值）
     一般乘一个小于1的**学习率**（调整一下步长）
$$\theta_{t+1}=\theta _{t}-\alpha_{t}\triangledown f(\theta_{t})$$


##  过拟合的解决办法
1. **减少特征**：删除与目标不相关的 特征，如一些特征选择方法：e.g. PCA降维。
2. **Early stopping**：防止过度拟合。 比如连续10次没达到最佳，就可以停止迭代了。
3. 更多的训练样本
4. 重新清洗数据：变顺序、降噪等。
5. **Dropout**：通过修改神经网络本身。
    -  随机删除一些隐藏层神经元，认为他们不存在。（不真的删）
    - 下一次继续随机。
    - 通过修改ANN中隐藏层的神经元个数来防止ANN的过拟合。
