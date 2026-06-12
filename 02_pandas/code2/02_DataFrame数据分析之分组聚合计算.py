import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
df.groupby("分组字段")["要聚合的字段"].聚合函数()
df.groupby(["分组字段", "分组字段2", ...])[["要聚合的字段", "要聚合的字段2", ...]].聚合函数()
上述类似mysql：
SELECT deptno,AVG(sal),MIN(sal),MAX(sal)  FROM emp GROUP BY deptno

pandas 聚合函数 = 对数据做统计：求和、平均、最大、最小、计数、分位数等。
比如：
sum()	求和
mean()	平均值
median()	中位数
count()	非空数量
size()	总行数（不管空值）
min()	最小值
max()	最大值
std()	标准差
var()	方差
nunique()	去重后的数量
'''

# ===================== 关键：让 pandas 完整显示所有内容 =====================
# pd.set_option('display.max_columns', None)   # 显示所有列
# pd.set_option('display.max_rows', None)      # 显示所有行
# pd.set_option('display.width', None)         # 不限制宽度
# pd.set_option('display.max_colwidth', None)  # 不限制列内容宽度
# ============================================================================


#初始化： 读取天气数据
df = pd.read_csv("../data/weather.csv")
print("weather.csv初始数据：\n",df)
# 将date转换为 年-月 的格式
df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
print("添加month列后新数据:\n",df)

######################################
#【1】 将数据按月分组，并统计最大温度和最小温度的平均值

# ① 分组：指定分组字段进行分组,本例按month分组，返回一个分组对象(DataFrameGroupBy)
df_groupby_month = df.groupby("month")
#print("指定分组字段进行分组,本例按照month分组:\n",df_groupby_month.value_counts())
print()
# ② 取字段：从分组对象中选择特定的列
month_temp = df_groupby_month[["temp_max", "temp_min"]]
#print("month_temp:\n",month_temp.value_counts())
# ③ 做聚合：对每个列求平均值，调用聚合函数 进行mean()	平均值统计
month_temp_mean = month_temp.mean()
print("对每个列求平均值，调用聚合函数 进行统计:\n",month_temp_mean)

print("*" * 50)
#
# 一条龙聚合版，以上代码可以写在一起
month_temp_mean = df.groupby("month")[["temp_max", "temp_min"]].mean()
print("一条龙聚合版:\n",month_temp_mean)

print("*" * 50)
#【2】分组频数计算统计每个月不同天气状况的数量。nunique()去重后的数量
# 公式：df.groupby("分组字段")["要聚合的字段"].聚合函数()
print("统计每个月不同天气状况的数量:\n",df.groupby("month")["weather"].nunique())