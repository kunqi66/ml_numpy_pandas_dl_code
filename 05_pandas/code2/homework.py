import pandas as pd
# 家庭作业：
# df.loc[:, "precipitation"]  # 获取所有行，列标签为precipitation的数据
# df.iloc[:, [3, 5, -1]]  # 获取所有行，列位置为3，5，最后一位的数据
# df.iloc[:10, 2:6]  # 获取前10行，列位置为2、3、4、5的数据
# df.loc[:10, ["date", "precipitation", "temp_max", "temp_min"]]  # 通过行列标签获取数据


# 家庭作业，自己搞定，O(∩_∩)O
# 按year升序，temp_max降序排序+按year去重
# 先按 year 升序 → 年份从小到大排
# 再按 temp_max 降序 → 同一年里，温度从高到低排
# 上两步结果：每一年的最高温度那一行，都会排在每一年的最上面
# drop_duplicates(subset=["year"])  参数subset=["year"] → 只看 year 这一列是否重复
# 作用：按年份去重，若是重复的年份，只保留第一行，后面全部删掉
# print(df.sort_values(by=["year", "temp_max"], ascending=[True, False]).drop_duplicates(subset=["year"]))
df = pd.read_csv("./data/weather.csv")
print(df.head())

df['year'] = pd.to_datetime(df['date']).dt.to_period("Y").astype(str)
print(df.head())
ans = df.sort_values(['year','temp_max'],ascending=[True, False]).drop_duplicates(subset=['year'])
print(type(ans))
print(ans)


# 家庭作业，自己思考懂......
# 8）薪资的分布
# print(df["salary"].mean())  # 平均值
# print(df["salary"].std())  # 标准差
# print(df["salary"].median())  # 中位数
# 9）找出平均薪资最高的部门id
# print(df.groupby("department_id")["salary"].mean().nlargest(1))  # 平均薪资最高的部门

