import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
本节类似mysql的表结构的修改
'''

#设置行索引 创建DataFrame时如果不指定行索引，pandas会自动添加从0开始的索引。
def setRowIndexDefault():
    df = pd.DataFrame({"age": [20, 30, 40, 10],
                       "name": ["张三", "李四", "王五", "赵六"],
                       "id": [101, 102, 103, 104]})
    print(df)

# 通过set_index()设置行索引
# inplace  是否进行原地操作，
# 如果值是True，直接在原有DataFrame上进行修改，
# 如果值是False，返回的是新创建DataFrame对象
def setRowIndexBySetIndex():
    df = pd.DataFrame({"age": [20, 30, 40, 10],
                       "name": ["张三", "李四", "王五", "赵六"],
                       "id": [101, 102, 103, 104]})
    print(df)
    print("==================")
    # 设置行索引
    df.set_index("id", inplace=True)
    print(df)

# 通过reset_index()重置行索引
def setRowIndexByReSetIndex():

    df = pd.DataFrame({"age": [20, 30, 40, 10],
                       "name": ["张三", "李四", "王五", "赵六"],
                       "id": [101, 102, 103, 104]},
                      index=[111, 122, 133, 144])
    print(df)
    print("==================")
    df.reset_index(inplace=True)  # 重置索引
    print(df)

# 修改行索引名和列名
def updateRowIndexAndColumnName():

    df = pd.DataFrame({"age": [20, 30, 40, 10],
                       "name": ["张三", "李四", "王五", "赵六"],
                       "id": [101, 102, 103, 104]})
    print(df)

    # 第一写法：通过rename()修改行索引名和列名
    df.set_index("id", inplace=True)
    print(df)
    df.rename(index={101: "一", 102: "二", 103: "三", 104: "四"},
              columns={"age": "年龄", "name": "姓名"},
              inplace=True)
    print(df)

    # 第二写法：将index和columns重新赋值
    # df.set_index("id", inplace=True)
    # print(df)
    # df.index = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ"]
    # df.columns = ["年齡", "名稱"]
    # print(df)

# 添加列
def addColumn():
    df = pd.DataFrame({"age": [20, 30, 40, 10],
                       "name": ["张三", "李四", "王五", "赵六"],
                       "id": [101, 102, 103, 104]})
    print(df)
    # 通过 df[“新的列名”] 添加列。
    df["phone"] = [1111, 2222, 3333, 4444]
    print(df)

# 删除行列
# df.drop(删除目标, axis=参数)
# axis=1   →   删 列（column）
# axis=0   →   删 行（index）
def delColumn():
    df = pd.DataFrame({"age": [20, 30, 40, 10],
                       "name": ["张三", "李四", "王五", "赵六"],
                       "id": [101, 102, 103, 104]})
    # 通过 df[“列名”] 添加列。
    df["phone"] = [1111, 2222, 3333, 4444]
    print(df)
    print("==================")
    #通过df.drop(“列名”, axis = 1) 删除
    print("删除phone，axis=1 →删 列（column）\n",df.drop("phone", axis=1))

    #删除行（删第0行）
    print("删除索引0的行：\n",df.drop(0, axis=0))

# 插入列
def insertColumn():
    # 通过 insert(loc, column, value) 插入。该方法没有inplace参数，直接在原数据上修改。
    # loc → 插在第几列
    # column → 新列叫什么
    # value → 这一列填什么数据
    df = pd.DataFrame({"age": [20, 30, 40, 10],
                       "name": ["张三", "李四", "王五", "赵六"],
                       "id": [101, 102, 103, 104]})
    # 在原表格最左边(loc=0)插入一列叫 phone，值 = 年龄 × 行号索引
    df.insert(loc=0, column="phone", value=df["age"] * df.index)
    print(df)


if __name__ == '__main__':
    #setRowIndexDefault()

    #setRowIndexBySetIndex()

    #setRowIndexByReSetIndex()

    #updateRowIndexAndColumnName()

    #addColumn()

    #delColumn()

    insertColumn()