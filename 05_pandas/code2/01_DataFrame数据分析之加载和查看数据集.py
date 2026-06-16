import pandas as pd

'''
../data/weather.csv使用weather（天气）数据集。其中包含6个字段：
	date：日期，年-月-日格式。
	precipitation：降水量。
	temp_max：最高温度。
	temp_min：最低温度。
	wind：风力。
	weather：天气状况。
'''
# ===================== 关键：让 pandas 完整显示所有内容 =====================
# pd.set_option('display.max_columns', None)   # 显示所有列
# pd.set_option('display.max_rows', None)      # 显示所有行
# pd.set_option('display.width', None)         # 不限制宽度
# pd.set_option('display.max_colwidth', None)  # 不限制列内容宽度
# ============================================================================

# 读取天气数据
df = pd.read_csv("./data/weather.csv")

# 属性操作
print("查看df类型:\n",type(df))
print("weather.csv初始数据：\n",df)
print("查看df形状：\n",df.shape)
print("查看df的列名：\n",df.columns)
print("查看df各列数据类型：\n",df.dtypes)

# 方法说明
# 通过head()、tail()获取前n行或后n行 略
#
# 获取一列或多列数据
# （1）加载一列数据
aa = df["date"]
print("df[date]加载一列数据返回的是Series: ",type(aa))
print()
# （2）加载多列数据
aa = df[["date"]]
print("df[[date]]加载多列数据返回的是DataFrame: ",type(aa))
# 获取多列数据，多列数据返回的是DataFrame
print(df[["date", "temp_max", "temp_min"]])
print()
# 3）按行获取数据 ,去掉表头后第一行数据为index=零开始计数
#（1）loc：通过行标签获取数据
print("df.loc[1]获取行标签为1的数据: \n",df.loc[1])
print()
print("df.loc[[1, 10, 100]]获取行标签分别为1、10、100的数据: \n",df.loc[[1, 10, 100]])
#（2）iloc：通过行位置获取数据
# 获取行位置为3的数据
print("df.iloc[3]获取行位置为3的数据: \n",df.iloc[3] )
# 获取行位置为最后一位的数据
print("df.iloc[-1]获取行位置为最后一位的数据: \n",df.iloc[-1])


# 4）获取指定行与列的数据
# df.loc[1, "precipitation"]  # 获取行标签为1，列标签为precipitation的数据
print("获取行标签为1，列标签为precipitation的数据: \n",df.loc[1, "precipitation"])

# 家庭作业：
# df.loc[:, "precipitation"]  # 获取所有行，列标签为precipitation的数据
# df.iloc[:, [3, 5, -1]]  # 获取所有行，列位置为3，5，最后一位的数据
# df.iloc[:10, 2:6]  # 获取前10行，列位置为2、3、4、5的数据
# df.loc[:10, ["date", "precipitation", "temp_max", "temp_min"]]  # 通过行列标签获取数据

