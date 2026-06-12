import numpy as np

# 数组相乘进行的是对位乘法
def arrayMulti():
    # 通过*运算符和np.multiply()对两个数组相乘进行的是对位乘法而非矩阵乘法运算。
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(arr1.shape, arr2.shape)
    print(arr1)
    print(arr2)
    print("-----数组相乘：两个数组相乘进行的是对位乘法")
    print(arr1 * arr2)
    print(np.multiply(arr1, arr2))
    # print()

def matrixMulti():
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(arr1)
    print(arr2)
    print("-----矩阵乘法：前行 × 后列，对应相乘再相加")
    # 使用np.dot() 或者 ndarray类型变量.dot() 或者 @可以进行矩阵乘法运算。
    #print(np.dot(arr1, arr2))
    #print(arr1.dot(arr2))
    print(arr1 @ arr2)
    '''
    1×5+2×7=19
    1×6+2×8=22
    3×5+4×7=43
    3×6+4×8=50
    '''


if __name__ == '__main__':
    #arrayMulti()
    matrixMulti()