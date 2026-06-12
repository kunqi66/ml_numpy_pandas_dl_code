import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame(
    data={"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"]},
    columns=["name", "age"],
    index=[101, 104, 103, 102],
)
print(df["age"] > 25)
print(df[df["age"] > 25])
