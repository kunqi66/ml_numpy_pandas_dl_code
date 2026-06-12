import numpy as np

# 2.8 基本运算

def baseOperationFun():
    # numpy中的数组不用编写循环即可执行批量运算，称之为矢量化运算。
    # 叠加运算即可，大小相等的数组之间的任何算术运算都会将运算应用到元素级。
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr1 * arr2)
    print(arr1 / arr2)
    print()

def baseOperationByCoefficient():
    #数组与标量的算术运算会将标量值传播到各个元素，不同大小的数组之间的运算叫做广播。
    # 类似看作矩阵变为一排，人人有份
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr1 + 100)
    print(arr1 - 100)
    print(arr1 * 100)
    print(arr1 / 100)

# 广播机制是 NumPy 中一个强大的特性，它允许在不同形状的数组之间进行元素级运算
def broadcastFun():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([[4], [5], [6]])
    print(arr1.shape)
    print(arr2.shape)# 3行1列
    print(arr1 + arr2)

    '''
    上述运算步骤细分拆解：
    第一步：自动补齐维度（左边补 1）
    arr1 (3,) → 补齐成 (1, 3)
    arr2 (3,1) → 保持 (3, 1)

    第二步：广播自动扩展成一样大
    arr1 从 (1,3) 扩展成 (3,3)
    沿着行复制 3 次
    [1,2,3]
    [1,2,3]
    [1,2,3]
    arr2 从 (3,1) 扩展成 (3,3)
    沿着列复制 3 次
    [4,4,4]
    [5,5,5]
    [6,6,6]

    第三步：逐元素相加
    [1,2,3]   +  [4,4,4]  =  [5,6,7]
    [1,2,3]   +  [5,5,5]  =  [6,7,8]
    [1,2,3]   +  [6,6,6]  =  [7,8,9]

    最终结果
    [[5 6 7]
     [6 7 8]
     [7 8 9]]

     总结
    (3,) → 横向扩展，复制行
    (3,1) → 纵向扩展，复制列
    最后变成同样大小的矩阵，再逐元素相加
    '''

def broadcastFunError():
    # 一维数组
    arr5 = np.array([1, 2, 3])  # 形状为 (3,)
    # 一维数组
    arr6 = np.array([4, 5])  # 形状为 (2,)
    try:
        result = arr5 + arr6
        print(result)
    except Exception as e:
        print(f"错误信息(3,) 和 (2,) 完全不兼容，不能运算: \n {e}")
        '''
        可以想象成要把两个矩阵拉伸成一样尺寸才能对应位置相加：
        [1,2,3] 是 3 个位置
        [4,5] 只有 2 个位置
        数量对不上，没法一一配对计算，程序不知道第 3 个数字拿谁去加，所以报错。
        '''


if __name__ == '__main__':
    #baseOperationFun()
    #baseOperationByCoefficient()
    #broadcastFun()
    broadcastFunError()
