import numpy as np

print("---套公式np.arange(起始, 终止, 步长间隔)")
array = np.arange(10)
array = np.arange(0,10)
array = np.arange(0,10,1)
print(array)
#
#获取索引为2的数据
print(array[2])


# 从索引 2开始到索引9(不包含)停止，间隔为2
print(array[slice(2,9,2)])


# 第2写法：从索引2开始到索引9(不包含)停止，间隔为2
print(array[2:9:2])

# 从索引2开始到最后(包含)，默认间隔为1,从索引 2 开始 → 取到最后一位（包含）
print(array[2::1])
# 请同学们回答
print(array[:8:1])
#
# array[2:9]取到 索引 9（不包含）
# array[2:-1]切片同样 不包含结束位，取到 最后一个元素之前（不包含最后一个）
print("array[2:9] ≡ array[2:-1] 从索引2开始到索引9(不包含)结束，默认间隔为1\n",array[2:-1])

# # 上面的都是一维数组，假如是二维的数组（矩阵）?
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(a)
print(a[0:2,1:3])