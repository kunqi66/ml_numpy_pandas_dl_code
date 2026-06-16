import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series 设计就是 name 显示在底部,DataFrame 才会把 name 显示成顶部列表头
def series_DataFrameDesc():
    seriesData = pd.Series([11, 12, 13, 14, 15], name="apple")
    print(seriesData)
    print("Series 设计就是 name 显示在底部,DataFrame 才会把 name 显示成顶部列表头")
    print()
    # 一键转 DataFrame
    df = seriesData.to_frame()
    print("to_frame()方法一键转 DataFrame\n",df)

    print()
    mango_series = pd.Series([4, 5, 6, 3, 1])
    apple_series = pd.Series([5, 4, 3, 0, 2])
    banana_series = pd.Series([2, 3, 5, 2, 7])
    # 通过Series创建DataFrame
    df = pd.DataFrame(
            data={
                "Mango": mango_series,
                "Apple": apple_series,
                "Banana": banana_series
                }
            )
    print(df)

def createDataFrame():
    # 直接通过字典创建DataFrame
    df = pd.DataFrame(data={
                "id": [101, 102, 103],
                "name": ["张三", "李四", "王五"],
                "age": [20, 30, 40]
                })
    print(df)
    print("*"*50)
    # 通过字典创建时指定列的顺序和行索引,data里面的column最好和columns里面指定的一样
    df = pd.DataFrame(
        data={"名字": ["张三", "李四", "王五"],"年龄": [20, 30, 40]},
        columns=["名字", "年龄"],
        #columns=["name", "age"],
        index=[101, 102, 103]
    )
    print(df)



if __name__ == '__main__':
    series_DataFrameDesc()

    createDataFrame()


