import numpy as np

'''
2.4.6 创建随机数数组
    Numpy随机函数 np.random
    
    rand()：生成0~1 均匀分布的随机数 / 数组
    randint()：生成指定范围的整数随机数 / 数组
    uniform()：生成自定义范围均匀分布的随机数 / 数组
    randn()：生成 ** 标准正态分布 (均值 0, 方差 1)** 的随机数 / 数组
    
    0~1 浮点数 → rand()
    指定范围整数 → randint()
    指定范围浮点数 → uniform()
    正态分布 → randn()
'''


# 1. random.rand() → 0~1  [0, 1)均匀分布
# # 4个0~1随机数
print("rand() [0,1):",np.random.rand(3,3))
print("rand(2行3列0~1):\n", np.random.rand(2,3))  # 2行3列0~1随机数


# 2. random.randint(最小值, 最大值, 个数) → 整数
# 1~9之间3个整数
print("randint(整数):",np.random.randint(1,9,3))



# 3. random.uniform(最小值, 最大值) → 自定义范围浮点数
# 2~5之间2个浮点数
print("uniform(浮点数):",np.random.uniform(2,5,2))





# # 4. random.randn() → 标准正态分布(均值0)
# # randn = random normal：标准正态分布采样，randn(n)：标准正态 N (0,1)，正负都有
# # 单个参数：randn(5) → 一维数组，共 5 个元素
# # 两个参数：randn(2,3) → 2 行 3 列二维数组
# # 三个参数：randn(2,3,4) → 三维数组，形状 (2,3,4)
# # 下面生成3个正态分布随机数
print("randn(正态分布(均值为0，标准差为1)):", np.random.randn(3))