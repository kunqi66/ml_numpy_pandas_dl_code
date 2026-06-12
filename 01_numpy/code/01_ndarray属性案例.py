import numpy as np


array1 = np.array([[1, 2, 3],[4,5,6]])
print(array1)
print("维度",array1.ndim)
print("形状",array1.shape)
print("个数",array1.size)
print("数据类型",array1.dtype)
print("变量类型",type(array1))
print("每个元素字节数大小",array1.itemsize)

# 1. 用 np.array() 函数 → 创建数组
arr = np.array([1, 2, 3])
# 2. 创建出来的 arr 它的类型 → 就是 np.ndarray
# np.ndarray只是一个类型,不能直接用来创建数组（底层用）,只用来判断类型 isinstance(arr, np.ndarray)
print(type(arr))  # <class 'numpy.ndarray'>
# 3. 验证
print(isinstance(arr, np.ndarray))  # True