import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
什么是布尔索引
    用一组 True/False 真假值，筛选 Series 数据
    True → 保留这一行
    False → 删掉这一行
    其中，NaN != 任何数字 → 结果都是 True
         NaN == 任何数字 → 结果都是 False
'''


seriesData = pd.Series([11,22,np.nan,None,44,22])
# 第1步：生成布尔条件,筛选大于 20 的数
cond = seriesData > 20
print(cond)
#第2步：布尔索引筛选
res = seriesData[cond]
print(res)

print("*"*40)
print("*"*40)



# 简写写法（日常最常用）,不用单独写 cond，直接一行：

# 筛选大于20
print("筛选大于20,seriesData[seriesData > 20]\n",seriesData[seriesData > 20])
# 筛选等于22,NaN == 任何数字 → 结果都是 False
print("筛选等于22,seriesData[seriesData == 22]\n",seriesData[seriesData == 22])
# 筛选不等于22,NaN != 任何数字 → 结果都是 True
print("筛选不等于22,seriesData[seriesData != 22]\n",seriesData[seriesData != 22])
# 不等于22且菲空值,过滤掉 NaN需要加一句seriesData.notna()
print("筛选不等于22且菲空值,seriesData[ (seriesData != 22) & seriesData.notna() ]\n",
      seriesData[ (seriesData != 22) & seriesData.notna() ])
