import numpy as np

# 2.7.3 比较函数
def compareFun():
    array1 = np.array([1,2,3,4,5])
    # np.any()	至少有一个元素满足指定条件，就返回True
    print("np.any()有一个元素满足指定条件，就返回True:\n", np.any(array1>3))
    # np.all()	所有的元素都满足指定条件，才返回True
    print("np.all()所有的元素满足指定条件，就返回True:\n", np.all(array1>3))


# 2.7.4 排序函数
# 重点:axis=0按列统计、axis=1按行统计。
def sortFun():
    array1 = np.array([
                        [0,2,-3],
                        [4,7,6],
                        [9,8,1]
                    ])
    #第一种写法： 就地排序（直接修改原数组）
    # 不写 axis 时，默认 axis=1，也就是按行内部原地排序；
    array1.sort()
    #array1.sort(axis=0)
    #array1.sort(axis=1)
    print(array1)

    #第二种写法（个人推荐使用）： np.sort()：返回排序后的副本（创建新的数组）
    # np.random.randint(大于等于最小值, 小于最大值, 形状)
    # 0 到 9 的随机整数矩阵，3 行 3 列形状
    array2 = np.random.randint(0,9,(3,3))
    print("初始排序前array2\n",array2)
    print("axis=1按行统计np.sort\n",np.sort(array2, axis=1))
    print("axis=0按列统计np.sort\n",np.sort(array2, axis=0))


# 2.7.5 去重函数
def uniqueFun():
    array1 = np.array([1,2,3,3,3,4,4,5])
    print(array1)
    # np.unique()：计算唯一值并返回有序结果。
    print(np.unique(array1))

if __name__ == "__main__":
    compareFun()

    sortFun()

    uniqueFun()