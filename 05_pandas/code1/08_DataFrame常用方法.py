import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#数据初始化 ，双aa索引合法，pandas 允许索引重复，不会直接报错冲突，不会初始化失败，能正常创建 DataFrame。
# 代码能跑、不冲突、不崩溃，但重复索引属于不良实践，日常数据分析、业务表尽量保证行索引唯一。
df = pd.DataFrame(data={"id": [101, 102, 103,104,105,106,101],
                        "name": ["张三", "李四", "王五","赵六","冯七","周八","张三"],
                        "age": [10, 10, 10, 40, None, 60,10]
                        },
                  index=["aa", "bb", "cc", "dd", "ee", "ff","aa"])
print("初始化\n",df)
print()

def m1():
    # head()	查看前n行数据，默认5行
    print("head(3)查看前3行数据，默认5行：\n", df.head(3))
    # tail()	查看后n行数据，默认5行
    # 略
    # isin()	元素是否包含在参数集合中
    print("isin()元素是否包含在参数集合中，对应坑位为true\n", df.isin([101, "赵六", 106]))
    # isna()元素是否为缺失值
    print("isna()元素是否为缺失值,Null位置为true\n", df.isna())
    # 指定列求和
    print("指定列名求和\n", df["id"].sum())
    # min()	最小值
    print("min()最小值\n", df["age"].min())
    # max()	最大值     略


def m2():
    # var()	方差,波动大小（平方级）
    # 非空数值求均值：(10+10+10+40+60+10) / 6 = 23.333...
    # 每个数与平均值的差的平方 (10-23.33)² = 177.69 | (40-23.33)²=277.8889 | (60-23.33)²=1344.6889
    # 总和 = 710.76（四份177.69） + 277.8889 + 1344.6889 = 2,333.3378
    # pandas默认ddof=1,分母 (6-1=5)
    #  总和➗(n-1) → 2,333.3378 ➗ 5 = 466.666...
    #  说明年龄波动非常大！大部分人 10 岁突然出现 40、60岁数据非常分散，所以方差很大。
    print("var()方差,计算age列的波动程度（样本方差）\n", df["age"].var())
    # mean()平均值
    print("指定列名age求平均值\n", df["age"].mean())
    # std()	标准差=方差开平方根,真实的平均波动距离（和原数据单位一样）,看数据 “平均偏离平均值多远”
    # 上步方法mean()平均值=23.33，标准差 ≈ 21.6意思是：年龄平均偏离平均值 21.6 岁左右！波动非常大。
    print("std()标准差:\n", df["age"].std())
    # median()	中位数= 把数据从小到大排好，中间那个数！10, 10, 10, 10, 40, 60
    # 数据个数是奇数：取正中间那个,数据个数是偶数：取中间两个的平均值
    print("median()中位数（age列从小到大排列后最中间的那个数）:\n", df["age"].median())
    # mode()	众数= 一组数据里【出现次数最多】的那个数！完全不管大小，只管次数
    print("mode() 众数:\n", df["age"].mode())
    # quantile()	指定位置的分位数，如求age列的 50% 分位数quantile(0.5)
    print("quantile(0.5)=50%分位数:\n", df["age"].quantile(0.5))


def m3():
    # describe()常见统计信息
    # 计算所有统计指标（count / mean / std / min / 四分位数 / max）时，直接自动跳过NaN，不参与运算
    print("describe()常见统计信息:\n",df.describe())
    print("*"*40)
    # info()    基本信息
    print(df.info())
    print()
    #value_counts()	每个元素的个数
    print("value_counts()	每个元素的个数:\n", df.value_counts())
    # count()	非空元素的个数
    print("count()	非空元素的个数:\n", df.count())
    # drop_duplicates()	去重
    print("drop_duplicates()去重:\n", df.drop_duplicates())
    # sample()默认随机抽取1行数据
    # df.sample(n=3)       # 随机取 3 行
    # df.sample(frac=0.5)  # 随机抽取 50% 数据
    # df.sample(random_state=42) # 固定随机结果，每次一样
    print("sample()随机采样:\n", df.sample())
    # replace()	用指定值代替原有值
    print("df.replace(要替换的值, 新值):\n", df.replace(np.nan, -11))
    print("*"*40)
    # equals()判断两个表格是否完全一模一样,列名+顺序+数据类型都必须相同+每一个单元格的值都必须相同
    df1 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
    df2 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
    print("equals()判断两个表格是否完全一模一样:", df1.equals(df2))
    print()

    df3 = pd.DataFrame(data={'A': [2, 5, 3, 7, 4], 'B': [1, 6, 2, 8, 3]})
    print("初始化df3\n", df3)
    # cummax = cumulative max → 累计最大值
    # axis=1 表示：按 行 计算（从左往右横着算）
    # 第 0 行：A=2，B=1
    # 第1列（A）：当前最大值 = 2
    # 第2列（B）：和前面最大值 2 比较 → 还是 2
    # ================
    # 第 1 行：A=5，B=6
    # A：最大值 5
    # B：比 5 大 → 变成 6
    print("cummax(axis=1)横着走,一路保留最大的那个数:\n", df3.cummax(axis=1))
    #print("cummax(axis=0)竖着走，遍历整列上方所有值，取至今最大值:\n", df3.cummax(axis=0))

    #cummin()	累计最小值   略
    #cumsum()	累计和
    print("cumsum()累计和:\n", df3.cumsum())
    #cumprod()	累计积   略

    # diff()一阶差分
    # 说明：对序列中的元素进行差分运算，用当前元素减去前一个元素得到差值，默认它会计算一阶差分，即相邻元素之间的差值。
    # 参数：
    # periods：整数，默认为 1。表示要向前或向后移动的周期数，用于计算差值。正数表示向前移动，负数表示向后移动。
    # axis：指定计算的轴方向。0 或 'index' 表示按列计算，1 或 'columns' 表示按行计算，默认值为 0。
    # A 列：
    #  2，
    #  5，
    #  3，
    #  7，
    #  4
    #   0 行：前面没数据 → NaN
    #   1 行：前面不够 2 行 → NaN
    #   2 行：3 - 2（0 行）= 1
    #   3 行：7 - 5（1 行）= 2
    #   4 行：4 - 3（2 行）= 1
    print("diff(periods=2)=当前行减去往上数第2行的值\n", df3.diff(periods=2))

def m4():
    # sort_index() = 按照【行号（索引）】从小到大排序
    print("sort_index()按行索引排序\n", df.sort_index())
    # sort_values()：按列内容排序（看表格里的数字），可传入列表来按多列排序，并通过ascending参数设置升序或降序
    print("sort_values()按列内容排序（看表格里的数字）\n", df.sort_values(by=["age", "id"], ascending=[True, False]))
    # nlargest (数量，列名)，从 age 列里找出【数值最大】的前 N 行，直接返回这几行数据！
    print("nlargest 取最大的N行数据:\n", df.nlargest(2, columns="age"))
    # nsmallest()	返回某列最小的n条数据，取出 age 列数值【最小】的 前 3 行 数据
    print("nsmallest(3, age) 取出年龄最小的3行：\n", df.nsmallest(3, columns="age"))


if __name__ == '__main__':
    #m1()
    #m2()
    #m3()
    m4()
