# 归一化的三种方式

**标准化**：为了去除数据的单位限制。

1. 其中最典型的是数据的归一化处理
     
     1.1 统一映射到[0,1]区间上。
     
     $$y = \frac{x-min}{(max-min)}$$
     
     1.2统一映射到[-1,1]区间上。
     
     $$y= \frac{x-x_{mean}}{(x_{max}-x_{min})}$$

2. 零均值归一化（zero-mean normalization）：z-score（标准正态分布）

     $$y = \frac{x-\mu}{\sigma}$$
