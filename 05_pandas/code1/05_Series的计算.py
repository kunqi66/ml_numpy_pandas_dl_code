import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series与标量运算，标量会与每个元素进行计算。
s1 = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
print(s1 * 10)

# Series与Series运算,会根据标签索引进行对位计算，索引没有匹配上的会用NaN填充。
s2 = pd.Series({"a": 1.1, "b": 2.2, "c": 3.3, "d": 4.4})
print(s1 + s2)



s3 = pd.Series({"a": 1.1, "b": 2.2, "c": 3.3, "d": 4.4},index=["a","b","c","x"])
print("s3----:\n",s3)
print(s1 + s3)













print()
s4 = pd.Series(     [1, 1, 1, 1])
                    #0  1  2  3
s5 = pd.Series([2, 2, 2, 2], index=[1, 2, 3, 4])
                       #1  2  3  4
print(s4 + s5)
