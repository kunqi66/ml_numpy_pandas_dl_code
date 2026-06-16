import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===================== 关键：让 pandas 完整显示所有内容 =====================
# pd.set_option('display.max_columns', None)   # 显示所有列
# pd.set_option('display.max_rows', None)      # 显示所有行
# pd.set_option('display.width', None)         # 不限制宽度
# pd.set_option('display.max_colwidth', None)  # 不限制列内容宽度
# ============================================================================

# 实现的数据的堆叠一句话记忆口诀
# axis=0 → 按行拼,上下叠
# axis=1 → 按列拼接，左右加

# 1）Series与Series连接
def mySeriesConcatSeries():
    s1 = pd.Series(["A", "B"], index=[1, 2])
    print(s1)
    s2 = pd.Series(["D", "E"], index=[4, 5])
    s3 = pd.Series(["G", "H"], index=[7, 8])

    #axis=0默认，按行竖着拼
    #把三个Series从上到下叠在一起，索引保留原来的索引
    print("===== axis=0默认，按行竖着拼=====")
    print(pd.concat([s1, s2, s3], axis=0))

    print()

    # axis=1按列横着拼
    # 每个 Series 变成一列，行索引会自动合并所有索引，没有值的位置填充 NaN
    print("===== axis=1按列横着拼=====")
    print("每个 Series 变成一列，行索引会自动合并所有索引，没有值的位置填充 NaN")
    print(pd.concat([s1, s2, s3], axis=1))

# 2）DataFrame与Series连接
def myDataFrameConcatSeries():
    # 创建DataFrame：2行2列，索引1、2
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    print("===== 原始 df1:\n",df1)

    # 创建Series：2个值，索引1、2，列名a（Series 必须带 name，按列拼接时才会有列名）
    s1 = pd.Series(data=[7, 10], index=[1, 2], name="a")
    print("===== 原始 s1:\n",s1)

    # 1. 默认按行拼接（axis=0）
    print("\n===== 按行拼接 df1 + s1 (axis=0) =====")
    print(pd.concat([df1, s1]))

    # 2. 按列拼接（axis=1）,Series 会被当成新列往右接
    print("\n===== 按列拼接 df1 + s1 (axis=1) =====")
    print(pd.concat([df1, s1], axis=1))

# 3）DataFrame与DataFrame连接，家庭作业，自己看懂。
def myDataFrameConcatDataFrame():
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    print("初始df1:\n",df1)
    df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])
    print("初始df2:\n",df2)

    # 1. 默认按行拼接（axis=0）
    print("\n===== 按行拼接 df1 + df2 (axis=0) =====")
    print(pd.concat([df1, df2]))

    # 2. 按列拼接（axis=1）
    print("\n===== 按列拼接 df1 + df2 (axis=1) =====")
    print(pd.concat([df1, df2], axis=1))

# 4）重置索引
def myResetIndex():
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    print("初始df1:\n",df1)
    df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])
    print("初始df2:\n",df2)
    print()
    print("\n===== 拼接前索引从上到下是1,2 1,2=====")
    print(pd.concat([df1, df2]))
    # 按行拼接 + 自动重置索引（最关键）ignore_index=True：忽略原来的索引，重新生成 0,1,2,3... 连续索引
    print("\n===== 拼接后（ignore_index=True）=====")
    print(pd.concat([df1, df2], ignore_index=True))

# 5）类似join的连接
# join 控制的是：按列拼接时，保留哪些索引
# outer：保留所有索引，没有的值 = NaN
# inner：只保留共同索引（交集）
def myConcatByJoin():
    df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
    print("初始df1:\n",df1)
    df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[2,3])
    print("初始df2:\n",df2)

    #默认：join="outer"（外连接）
    '''
    SELECT
        IFNULL(t1.idx, t2.idx) AS idx,
        t1.a AS t1_a,
        t1.b AS t1_b,
        t2.a AS t2_a,
        t2.b AS t2_b
    FROM t1
    FULL OUTER JOIN t2 ON t1.idx = t2.idx;
    '''
    print("\n===== 默认连接 join='outer' =====")
    print(pd.concat([df1, df2],axis=1))  # axis=1 才能看出join效果！

    #内连接：join="inner"
    '''
    SELECT
    t1.idx,
    t1.a AS t1_a,
    t1.b AS t1_b,
    t2.a AS t2_a,
    t2.b AS t2_b
    FROM t1
    INNER JOIN t2
    ON t1.idx = t2.idx;
    '''
    print("\n===== 内连接 join='inner' =====")
    print(pd.concat([df1, df2],axis=1, join="inner"))

if __name__ == '__main__':
    # 1）Series与Series连接
    #mySeriesConcatSeries()

    # 2）DataFrame与Series连接
    myDataFrameConcatSeries()

    # 3）DataFrame与DataFrame连接 ，家庭作业，自己看懂。
    #myDataFrameConcatDataFrame()

    # 4）重置索引
    #myResetIndex()

    # 5）类似join的连接
    myConcatByJoin()