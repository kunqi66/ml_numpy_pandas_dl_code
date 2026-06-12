import numpy as np

# 2.7.2 统计函数
def statisticalFunction():
    array1 = np.array([
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ])
    print("array1\n",array1)
    print("array1形状\n",array1.shape)
    array2 = np.array([1,2,3])
    print("array2\n",array2)
    print("array2\n",array2.shape)




    # 重点:axis=0按列统计、axis=1按行统计。
    # np.mean()	所有元素的平均值
    print("总和 ÷ 元素总个数:\n",np.mean(array1))
    print("axis=0按列求平均（纵向压缩）:\n",np.mean(array1, axis=0))
    print("axis=1按行求平均（横向压缩）:\n",np.mean(array1, axis=1))

    # np.sum()	所有元素的和
    print("元素总和:\n",np.sum(array1))
    # axis=0按列统计
    print("axis=0按列求和:\n",np.sum(array1,axis=0))
    # axis=1按行统计
    print("axis=1按行求和:\n",np.sum(array1,axis=1))
    # np.max()	所有元素的最大值
    print(np.max(array1))
    # np.min()	所有元素的最小值
    print(np.min(array1))


    #
    # ###################重点，提前给同学们上强度，进入机器学习，用在哪？###############
    # np.var () → 方差就是用来描述一组数据波动大小、离散程度的指标。
    # 数据越乱、越分散，方差越大，越整齐、越集中，方差越小
    print("所有元素的方差:\n", np.var(array2))  # 方差  0.666666...
    # np.std () → 标准差：方差开平方根	标准差单位和原数据一致，日常看波动优先用 np.std()
    print("所有元素的标准差:\n", np.std(array2))  # 标准差 0.816496...


    # 重点:axis=0按列统计、axis=1按行统计。
    # np.argmax()	最大值的下标索引值
    print("整个数组展平，最大值的下标索引值array1:\n", np.argmax(array1))
    '''
    逐列对比：axis=0 按列
    第 0 列：1、4、7 → 最大值 7，索引 2
    第 1 列：2、5、8 → 最大值 8，索引 2
    第 2 列：3、6、9 → 最大值 9，索引 2
    输出：[2 2 2]
    '''
    print("axis=0 按列找最大值索引:\n", np.argmax(array1, axis=0))



    '''
    逐行对比：axis=1 按行
    第 0 行：1、2、3 → 最大值 3，索引 2
    第 1 行：4、5、6 → 最大值 6，索引 2
    第 2 行：7、8、9 → 最大值 9，索引 2
    输出：[2 2 2]
    '''
    print("axis=1 按行找最大值索引:\n", np.argmax(array1, axis=1))
    # np.argmin()	最小值的下标索引值
    # 通过上一个，要求大家自学

    # np.cumsum()	返回一个一维数组，每个元素都是之前所有元素的累加和
    print("所有元素的累加和:\n", np.cumsum(array1))
    # np.cumprod()	返回一个一维数组，每个元素都是之前所有元素的累乘积
    print("所有元素的累乘积:\n", np.cumprod(array1))


if __name__ == '__main__':
    statisticalFunction()