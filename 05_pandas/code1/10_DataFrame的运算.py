import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DataFrame与标量运算,标量与每个元素进行计算。
df = pd.DataFrame(
    data={"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"]},
    columns=["name", "age"],
    index=[101, 104, 103, 102],
)
print(df * 2)


# DataFrame与DataFrame运算,根据标签索引进行对位计算，索引没有匹配上的用NaN填充。
df1 = pd.DataFrame(
    data={"age": [10, 20, 30, 40], "name": ["张三", "李四", "王五", "赵六"]},
    columns=["name", "age"],
    index=[101, 102, 103, 104],
)

df2 = pd.DataFrame(
    data={"age": [10, 20, 30, 40], "name": ["张三", "李四", "王五", "田七"]},
    columns=["name", "age"],
    index=      [102, 103, 104, 105],
)
print(df1 + df2)

