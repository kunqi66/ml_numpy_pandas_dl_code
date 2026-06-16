import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===================== 关键：让 pandas 完整显示所有内容 =====================
# pd.set_option('display.max_columns', None)   # 显示所有列
# pd.set_option('display.max_rows', None)      # 显示所有行
# pd.set_option('display.width', None)         # 不限制宽度
# pd.set_option('display.max_colwidth', None)  # 不限制列内容宽度
# ============================================================================

'''
nlargest(n, [列名1, 列名2, …])：按列排序的最大n个
nsmallest(n, [列名1, 列名2, …])：按列排序的最小n个
sort_values([列名1, 列名2, …], asceding=[True, False, …])：按列升序或降序排序
drop_duplicates(subset=[列名1, 列名2])：按列去重
'''


#初始化： 读取天气数据
df = pd.read_csv("./data/weather.csv")

#（1）找到最高温度最大的30天,通过nlargest()找出temp_max最大的30条数据。
print("通过nlargest()按列找出temp_max最大的30条数据:\n",df.nlargest(30, "temp_max"))

# （2）从最高温度最大的30天中找出最低温度最小的5天,通过nlargest()找出temp_min最小的5条数据。
print("最高温度最大的30天中找出最低温度最小的5天:\n",df.nlargest(30, "temp_max").nsmallest(5, "temp_min"))

#（3）找出每年的最高温度
df["year"] = pd.to_datetime(df["date"]).dt.to_period("Y").astype(str)  # 将date转换为 年 格式
print("添加year列后新数据:\n",df)
print()
print("把数据按年份分组 → 每组只看最高温度列 → 算出每一年的最高温度 → 输出结果:\n",
      df.groupby("year")["temp_max"].max())


# 家庭作业，自己搞定，O(∩_∩)O
# 按year升序，temp_max降序排序+按year去重
# 先按 year 升序 → 年份从小到大排
# 再按 temp_max 降序 → 同一年里，温度从高到低排
# 上两步结果：每一年的最高温度那一行，都会排在每一年的最上面
# drop_duplicates(subset=["year"])  参数subset=["year"] → 只看 year 这一列是否重复
# 作用：按年份去重，若是重复的年份，只保留第一行，后面全部删掉
# print(df.sort_values(by=["year", "temp_max"], ascending=[True, False]).drop_duplicates(subset=["year"]))
