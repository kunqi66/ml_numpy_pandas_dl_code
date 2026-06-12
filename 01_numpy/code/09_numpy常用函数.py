import numpy as np

# 2.7 numpy常用函数
def baseFunction():
    array1 = np.array([ [1,-2.8,3.5],[4,-5.1,6.7] ])
    print(array1,array1.dtype)
    # np.abs()	元素的绝对值，参数是 number 或 array
    print(np.abs(array1))
    # np.ceil()	向上取整，参数是 number 或 array
    print("向上取整:\n",np.ceil(array1))
    # np.floor()	向下取整，参数是 number 或 array
    print("向下取整\n", np.floor(array1))
    # np.isnan() 检测数组元素是否为 NaN（Not a Number，非数值） 的函数
    array3 = np.array([1.0, 2.0, np.nan, 4.0,np.nan, 6.0])
    # 检测哪些是 NaN
    print(np.isnan(array3))  # 输出: [False False  True False  True False]
    # 取反：找出哪些不是 NaN
    print(~np.isnan(array3))  # 输出: [ True  True False  True False  True]
    # np.multiply()	元素相乘，参数是 number 或 array。
    # 如果第二个参数传递的是number，原数组中所有元素乘以这个数字，返回新的数组；
    # 如果第二个参数也是一个数组，是将两个数组中对应位置的元素相乘，返回一个新的数组，其形状与输入数组相同。
    array4 = np.array([[1, 2, 3], [4,5,6]])
    print("元素相乘:\n",np.multiply(array4, array4))
    # np.divide()	元素相除，参数是 number 或 array
    print("divide元素相除:\n",np.divide(array4, 2))
    # np.where(condition, x, y)	三元运算符，x if condition else y
    print("三元运算符:\n",np.where(array4 > 3, 1, 0))
    print("*" * 60)
# # np.rint()/np.around()/np.round() 四舍六入五成双（银行家舍入,只有 x.5 才会不一样，其他小数都一样），
#     # 参数是 number 或 array,这个设计主要是为了在大量统计计算中减少累积误差，使得数据在整体上更均衡。
#     # 而传统的“四舍五入”总会把 0.5 往同一个方向（大）舍入，会造成系统性偏差。
# # 四舍六入五成双：
#     # ≤4 舍去
#     # ≥6 进位
#     # =5 → 正好为0.5时,看前一位是奇数还是偶数,偶舍奇入
    array2 = np.array([2.3,2.5, 3.5, 1.4, 11.6,7.5])
    print("四舍六入五成双\n",np.rint(array2))
    print("*" * 60)
    # 对 0.5, 1.5, 2.5, 3.5 进行四舍六入五成双
    # 规则：正好为0.5时，看整数部分，偶舍奇入
    print(np.round([0.5, 1.5, 2.5, 3.5]))    # 输出: [0. 2. 2. 4.]
    # 0.5 -> 0 (0是偶数，舍)
    # 1.5 -> 2 (1是奇数，入)
    # 2.5 -> 2 (2是偶数，舍)
    # 3.5 -> 4 (3是奇数，入)


if __name__ == "__main__":
    baseFunction()