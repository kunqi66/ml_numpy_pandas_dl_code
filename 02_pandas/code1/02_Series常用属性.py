import pandas as pd

'''
Series = 表的列 (Column),数据库中的一列数据加上行号,本质是带索引的一维数组 + 数据库列的属性
'''

seriesData = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"],name="atguigu_Series")
print("seriesData初始化内容:\n",seriesData)
print()

print("Series的索引对象:\n",seriesData.index)
print("Series的的值:\n",seriesData.values)
print("Series的维度:\n",seriesData.ndim)
print("Series的形状:\n",seriesData.shape)
print("Series的元素个数:\n",seriesData.size)
print("Series的名称:\n",seriesData.name)
print("*"*50)




print("显式索引，按标签索引或切片,左闭右闭:\n",seriesData.loc["a":"d"])

print("隐式索引，按位置索引或切片,左闭右开:\n",seriesData.iloc[0:3])

print("使用标签访问单个元素:\n",seriesData.at["a"])
print("使用位置访问单个元素:\n",seriesData.iat[3])