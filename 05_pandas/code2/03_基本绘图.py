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
df = pd.read_csv("./data/weather.csv")
print("weather.csv初始数据：\n",df)
# 将date转换为 年-月 的格式
df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
print("添加month列后新数据:\n",df)

# 一条龙聚合版，以上代码可以写在一起
month_temp_mean = df.groupby("month")[["temp_max", "temp_min"]].mean()
print("一条龙聚合版:\n",month_temp_mean)

# 绘图
month_temp_mean.plot()

#显示图表
plt.show()