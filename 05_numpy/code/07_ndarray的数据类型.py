import numpy as np

# 2.5 ndarray的数据类型

array1 = np.array([1, 2, 3])
# type(array1) 判断整个变量的类型
# array1.dtype 判断数组里每一个元素的存储类型
print(array1,type(array1),array1.dtype)

array2 = np.array([1, 2, 3.1])
print(array2,type(array2),array2.dtype)


array3 = np.array([1, 2, 3],dtype=np.float64)
print(array3,type(array3),array3.dtype)



array4 = np.array([1.1, 2.2, 3.3],dtype="i8")
print(array4,type(array4),array4.dtype)







#也可以使用ndarray.astype()方法转换数组的元素类型：
# 实际中慎用，容易精度丢失,了解即可，实际中不要使用，就当没学过
array5 = np.array([1.1, 2.1, 3.1], dtype=np.float64)
print(array5,type(array5),array5.dtype)
array6 = array5.astype(np.int64)
print(array6,type(array6),array6.dtype)
