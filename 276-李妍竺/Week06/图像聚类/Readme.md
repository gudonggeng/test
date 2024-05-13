# K-means

**目标：将数据点划分为K个类簇。**

经K-Means处理过的图像：
聚成K个簇类后，用每个簇的质心替换cuneiform所有像素点。这样就能**在不改变分辨率的情况下量化压缩图像颜色，实现图像颜色的层级分割**。几个K，就剩下几种颜色。

## K-Means的步骤：
1. 确定K值：要将数据聚成几个类簇（根据经验，人工分类）
2. 从数据集中随机选**K个数据点作为质心**（Centroid) (分组)
3. 分别计算**每个点到每个质心的距离**，将每个点划分到距离最近的质心。（分组）
4. 当每个质心都聚了一些点后，需要新的K个质心。算出每组的**平均值**作为新的质心（虚拟质心）
5. 迭代3、4，直到终止满足。（聚类结果不再发生变化）

## 调用接口

```
# 一般用于对现成的数据进行操作
from sklearn.cluster import KMeans

clf = KMeans(n_cluster=n)   #clf：分类器
y_pred = clf.fit_predict(x)  # 载入数据集x
```

**层次聚类**
**Hierachicalmethods**
按照层次分解顺序，分为：
- 自下而上：**凝聚的层次聚类算法。**
- 自上而下：分裂的层次聚类算法。

**凝聚的层次聚类流程：**
1. 将每个对象看作一类，计算两两之间的最小距离。
2. 将距离最小的两个类合并成一个新的类。
3. 重新计算新的类和所有类之间的距离
4. 重复2、3直到所有类最后合并成一类。

**判断依据**
树状图，想分几类，就从上往下数有几根竖线时进行分割。对应竖线下面所连接的为一类。

## 核心算法
```
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, flaster

 - linkage(y, method=’single’, metric=’euclidean’) 共包含3个参数: 
  1. y是距离矩阵,可以是1维压缩向量（距离向量），也可以是2维观测向量（坐标矩阵）。      若y是1维压缩向量，则y必须是n个初始观测值的组合，n是坐标矩阵中成对的观测值。  
  2. method是指计算类间距离的方法。
    - 'single': 最邻近距离（范数距离）
    - 'complete':最远临点
    - 'average'：平均
    - 'ward': 离差平方和
    - 'centroid': 二范数距离
  3. metric:单位  str 或function

 - fcluster(Z, t, criterion=’inconsistent’, depth=2, R=None, monocrit=None) 
   1.第一个参数Z是linkage得到的矩阵,记录了层次聚类的层次信息; 
   2.t是一个聚类的阈值-每个簇类距离不超过t
   3.criterion=’inconsistent’ 预设的
   - 返回值：数组：每个元素分别属于哪个类别
 - dendrogram: 绘制层次聚类树状图
 ```
