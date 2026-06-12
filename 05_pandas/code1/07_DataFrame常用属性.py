import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(data={
            "id": [101, 102, 103],
            "name": ["张三", "李四", "王五"],
            "age": [20, 30, 40]
            },
            index=["aa", "bb", "cc"])
print("初始(等价select * from t_user):\n",df)
print("只需要id和name(等价select id,name from t_user):\n",df[["id","name"]])


######【第一组】 一眼过
# index	DataFrame的行索引
print("index DataFrame的行索引:",df.index)
# columns	DataFrame的列标签
print("columns	DataFrame的列标签:",df.columns)
# values	DataFrame的值
print("values	DataFrame的值:\n",df.values)
# ndim	DataFrame的维度
print("ndim	DataFrame的维度:",df.ndim)
# shape	DataFrame的形状
print("shape DataFrame的形状:",df.shape)
# size	DataFrame的元素个数
print("size	DataFrame的元素个数:",df.size)
# dtypes	DataFrame的元素类型
print("dtypes	DataFrame的元素类型:",df.dtypes)
print()
######【第二组】
# T	行列转置
print("初始:\n",df)
print("T	行列转置:\n",df.T)
#
# print()
# ######【第三组】
# loc[] 显式索引，按行列标签索引或切片 逗号前是行切片规则，逗号后是列切片规则
print("loc[]显式索引，按行列标签索引或切片:\n",df.loc["aa":"bb","name":])
print("loc[]显式索引，按行列标签索引或切片v2:\n",df.loc[:,["id","name"]])
print("loc[]显式索引，按行列标签索引或切片v3:\n",df.loc[:,["age"]])
print()
# iloc[]    隐式索引，按行列位置索引或切片
print("iloc[]隐式索引，按行列位置索引或切片:\n",df.iloc[0:2,0:2])
# at[]	使用行列标签访问单个元素
print("at[]使用行列标签访问单个元素:\n",df.at["bb","name"])
# iat[]	使用行列位置访问单个元素
print("iat[]使用行列位置访问单个元素:\n",df.iat[0,0])
