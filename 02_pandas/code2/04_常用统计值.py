import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===================== 关键：让 pandas 完整显示所有内容 =====================
# pd.set_option('display.max_columns', None)   # 显示所有列
# pd.set_option('display.max_rows', None)      # 显示所有行
# pd.set_option('display.width', None)         # 不限制宽度
# pd.set_option('display.max_colwidth', None)  # 不限制列内容宽度
# ============================================================================

#初始化： 读取天气数据
df = pd.read_csv("../data/weather.csv")
#print("weather.csv初始数据：\n",df)
# 将date转换为 年-月 的格式
df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
print("添加month列后新数据:\n",df)
print()

print("df.describe()查看常用统计信息:\n",df.describe())
print()
print("df.describe().T查看常用统计信息行列转置:\n",df.describe().T)

# 可通过include参数指定要统计哪些数据类型的列。
# 家庭作业，自己搞定，so easy O(∩_∩)O
#df.describe(include="all")  # 统计所有列
#df.describe(include=["float64"])  # 只统计数据类型为float64的列