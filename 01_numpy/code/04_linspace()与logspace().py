import numpy as np

'''
 2.4.5 linspace()与logspace()
一句话总结
    linspace() 是线性等分生成指定数量的等差数列；
    logspace() 是对数等分生成指定数量的等比数列（默认基于 10 的幂）。
    
    极简用法
    np.linspace(起始, 终止, 数量)：线性均分，包含终止值
    np.logspace(起始次幂, 终止次幂, 数量)：对数均分，值 = 10^i
    
    核心记忆
    linspace：看总个数均分，包含终止值，均匀增长
    logspace：按10 的幂次均分，生成等比数列
'''

# 1. linspace：0到10，均分生成5个数（线性）,默认 endpoint=True → 包含终止值 10
# np.linspace(起始, 终止, 数量)：线性均分，包含终止值
# 要包含终止值 → 用默认 endpoint=True
# 不要包含终止值 → 写 endpoint=False
arr1 = np.linspace(0,10,5)
print("linspace 线性等分endpoint=True（包含10）：\n", arr1)


# 2. endpoint=False → 不包含终止值 10
arr2 = np.linspace(0, 10, 5,endpoint=False)
print("linspace 线性等分endpoint=False（不包含10）：\n", arr2)

#
# 3. logspace：2^1 到 2^5，均分生成5个数（对数/等比），base=2以2为底
arr3 = np.logspace(1, 5, 5,base=2)
print("\nlogspace 对数等分：\n", arr3)

print()
