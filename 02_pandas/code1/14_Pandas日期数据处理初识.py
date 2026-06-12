import pandas as pd

# ===================== 关键：让 pandas 完整显示所有内容 =====================
# pd.set_option('display.max_columns', None)   # 显示所有列
# pd.set_option('display.max_rows', None)      # 显示所有行
# pd.set_option('display.width', None)         # 不限制宽度
# pd.set_option('display.max_colwidth', None)  # 不限制列内容宽度
# ============================================================================

# GMV 全称：Gross Merchandise Volume 商品交易总额，电商平台核心统计指标
df = pd.DataFrame({"gmv":[100,200,300,400],
                   "trade_date":["2025-01-06","2023-10-31","2023-12-31","2023-01-05"]})

df["ymd"] = pd.to_datetime(df["trade_date"])
print("将字符串字段转换为日期类型:\n",df)

df['yy']=df['ymd'].dt.year
df['mm']=df['ymd'].dt.month
df['dd']=df['ymd'].dt.day
print("获取年月日:\n",df)

df['week']=df['ymd'].dt.day_name()
print("获取星期:\n",df)

df['quarter']=df['ymd'].dt.quarter
print("获取日期所在季度:\n",df)

df['monthEnd']=df['ymd'].dt.is_month_end
df['yearEnd']=df['ymd'].dt.is_year_end
print("判断日期是否月底年底:\n",df)

print()
print("*"*50)
'''
3.4.3 to_period()获取统计周期
freq：这是 to_period() 方法最重要的参数，用于指定要转换的时间周期频率
常见的取值如下：
	"Y"：按年周期，如 2024-07-20 会转换为 2024 。
	"M"：按月周期，像 2024-05-15 会转换为 2024-05。
	"Q"：按季度周期，一年分为四个季度，日期会转换到对应的季度周期，例如 2024Q2 。
	"W"：按周周期，通常以周日作为一周的结束，比如日期落在某一周内，就会转换为该周的周期表示。
	"D"：按天周期，例如 2024-01-01 会转换为 2024-01-01 这个天的周期。
'''
df["ystat"] = df["ymd"].dt.to_period("Y")
df["mstat"] = df["ymd"].dt.to_period("M")
df["qstat"] = df["ymd"].dt.to_period("Q")
df["wstat"] = df["ymd"].dt.to_period("W")
print(df)
