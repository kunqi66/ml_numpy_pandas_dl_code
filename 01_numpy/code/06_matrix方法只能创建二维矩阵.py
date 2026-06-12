import numpy as np

'''
2.4.7 matrix()
一句话总结
    numpy 的 np.matrix() 只能创建二维矩阵，不支持一维、三维及以上，强行传高维会直接报错；
    而 np.array() 可以任意 N 维。
'''
def mymatrix():
    # 正常：二维，合法
    m1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("二维合法：\n", m1)

    # 想创建一维 → 自动转成二维 (1行N列)
    # 传入一维数据，会自动包装成 1 行多列 的二维矩阵；
    m2 = np.matrix([1,2,3,4,5,6])
    print("m2 内容:\n", m2)  #[[1 2 3 4 5 6]]
    print("m2 形状:", m2.shape)  #(1, 6)
    #演示重构一下看看
    print(m2.reshape(2,3))









    # 真正 1行1列
    m3 = np.matrix([5])
    print("\nm3 形状:", m3.shape)  # (1, 1)
    print("m3 内容:\n", m3)  # [[5]]

    # 想创建三维尝试给 matrix 传 3 维数据 → 直接报错
    try:
        m4 = np.matrix([[[1,2,3],[4,5,6],[7,8,9]]])
    except ValueError as e:
        print(e)
        raise e


if __name__ == '__main__':
    mymatrix()