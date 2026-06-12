import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Series = 表的列 (Column),数据库中的一列数据加上行号,本质是带索引的一维数组 + 数据库列的属性
'''

seriesData = pd.Series([11,22,np.nan,None,44,22],index=['a','b','c','d','e','f'])
print("seriesData初始化数据:\n",seriesData)
print()

def doSeriesMethodV1():
    # head()	查看前n行数据，默认5行
    print("head()查看前n行数据，默认5行\n", seriesData.head())
    # tail()	查看后n行数据，默认5行
    # 略
    # isin(列表/集合)	元素是否包含在参数集合中,NaN 和 None 永远不匹配（isin 不认空值）
    print("isin()元素是否包含在参数集合中:\n", seriesData.isin([11, 22]))
    # isna()	判断每个元素是不是【空值】（ 是不是空值？（NaN / None → True））
    print("isna()判断每个元素是不是【空值】:\n", seriesData.isna())
    # sum()求和，自动忽略NaN/None空值，只加有效数字。
    print("sum()只累加有效数字求和（自动忽略NaN/None空值）:\n", seriesData.sum())
    # mean() 只用非空数值求平均值，默认自动忽略缺失值；设置 skipna=False 时，含空值整体直接返回 NaN
    print("mean()只用非空数值求平均值（总和：99，有效个数：4 平均值：99÷4=24.75）:\n", seriesData.mean())
    # min()	最小值  略
    # max()	最大值 略

    print()

    # var()	波动大小（平方级）,默认样本方差（除以 n-1） 自动忽略 NaN / None
    # 方差是衡量数据波动大小、离散程度。数值越分散 → 方差越大
    # 非空数值：11, 22, 44, 22，有效个数：4个 平均值：99÷4=24.75
    # 每个数与平均值的差的平方 (11-24.75)² = 189.0625|(22-24.75)² = 7.5625|(44-24.75)² = 370.5625|(22-24.75)² = 7.5625
    # 样本方差（默认）总和574.75 ➗ (4-1) = 574.75 / 3 = 191.58333333333334
    print("var()方差:\n", seriesData.var())
    # std()	标准差=方差开平方根,真实的平均波动距离（和原数据单位一样）
    print("std()标准差:\n", seriesData.std())
    # median()	把数据从小到大排序，取中间值,默认 skipna=True：自动忽略 NaN、None
    # 偶数中间两个数相加除以 2,奇数直接取正中间那一个数
    print("median()中位数:\n", seriesData.median())
    # mode() 众数（一组数据里出现次数最多的数），，
    # 可以有一个或多个众数（如果有多个值出现的频率相同且都是最高频率）返回的是Series，它不是单个数值，自动忽略 NaN/None
    print("mode()众数，出现次数最多的值:\n", seriesData.mode())





    # quantile(q,interpolation)指定位置的分位数
    # 数据排序后在q%位置上的数值, 分位数可以不是原始数据，它是按比例算出来的 “位置值”,自动忽略 NaN/None
    # 参数说明：
    # q：要算的分位数（0 到 1 之间的浮点数或浮点数列表）
    #   quantile(0.25) = 1/4 位置
    #   quantile(0.5) = 中位数
    #   quantile(0.75) = 3/4 位置
    # interpolation：插值方式（怎么算中间位置），最常用 3 种
    # linear（默认）线性插值，最常用
    # midpoint（取中间两个数的平均值（纯中位数）
    # nearest（取最近的那个数)
    # 案例说明
    # Pandas 默认位置公式：pos=(n−1)×q：quantile(q, interpolation='linear')
    '''
    过程分析：
    计算 quantile(0.25) = 0.25 分位数,推导过程
    1)位置 = (4 - 1) × 0.25
         = 3 × 0.25
         = 0.75
    2)位置 0.75 在哪里？
    排序数据：
    索引 0 → 11
    索引 1 → 22
    索引 2 → 22
    索引 3 → 44
    0.75 在 0 和 1 之间
    低位：索引 0 → 11
    高位：索引 1 → 22
    位置是 0.75，意思是：从 索引0（值11） 往 索引 1（值22） 走 75% 的距离
    3) 默认线性插值计算
    结果 = 低位 + (高位 - 低位) × 小数部分
         = 11 + (22 - 11) × 0.75
         = 11 + 11 × 0.75
         = 11 + 8.25
         = 19.25
    4) 结论：
    上面19.25 和数据有什么关系？
    一句话：分位数不是从数据里直接挑数字，而是按位置比例算出来的 “分界值”。它可以不在原始数据里！
    把 4 个数字排好想象成一条线：
    11 ---- 19.25 ---- 22 ------ 22 ------ 44
    0.25 分位数 = 整条数据从左数 25% 位置的值，这个位置刚好落在 11 和 22 之间，所以算出来是 19.25。
    '''
    print("quantile(0.25):\n", seriesData.quantile(0.25))  # 19.25
    print("quantile(0.5):\n", seriesData.quantile(0.5))  # 22.0
    print("quantile(0.5,interpolation='midpoint'):\n", seriesData.quantile(0.5, interpolation='midpoint'))  # 22.0
    '''
    计算 quantile(0.75) = 0.75 分位数,推导过程
    1)位置 = (4 - 1) × 0.75
         = 3 × 0.75
         = 2.25
    2)位置 2.25 在哪里？
    排序数据：
    索引 0 → 11
    索引 1 → 22
    索引 2 → 22
    索引 3 → 44
    位置 2.25 在坑位 2 和 3 之间
    低位：索引 2 → 22
    高位：索引 3 → 44
    整数部分：2
    小数部分：0.25
    3) 线性插值计算
    结果 = 低位 + (高位 - 低位) × 小数部分
         = 22 + (44 - 22) × 0.25
         = 22 + 22×0.25
         = 27.5
    '''
    print("quantile(0.75):\n", seriesData.quantile(0.75))  # 27.5


def doSeriesMethodV2():
    # describe()	常见统计信息，一键统计汇总
    print("describe()统计信息:\n", seriesData.describe())
    # value_counts()	每个元素的个数
    print("value_counts()每个元素的个数:\n", seriesData.value_counts())
    # count()	非缺失值元素的个数，如果要包含缺失值，用len()
    print("count()非缺失值元素的个数:\n", seriesData.count())
    # drop_duplicates()	去重
    print("drop_duplicates()去重:\n", seriesData.drop_duplicates())
    # unique()	去重后的数组
    print("unique()去重后的数组:\n", seriesData.unique())
    # nunique()	统计【不重复的非空元素】有多少个,如果你想把 NaN 也算进去加参数 dropna=False
    print("nunique()不重复的非空元素个数:\n", seriesData.nunique())
    # sample()	随机打乱顺序抽样:从 Series 里随机抽几条数据,空值 NaN/None 也会参与抽样，不会自动过滤
    # 参数：random_state=任意整数：种子固定，抽样永远一样数字随便选
    print("sample()随机抽样:\n", seriesData.sample())
    print("sample(random_state=42)：固定种子 → 每次抽样结果完全一样可复现:\n", seriesData.sample(random_state=42))
    # sort_index()	按索引排序
    print("sort_index()按索引排序:\n", seriesData.sort_index())
    # sort_values()	按值排序
    print("sort_values()按值排序:\n", seriesData.sort_values())
    # replace (旧值，新值) = 全局替换数据里的值，不会修改原数据，只返回新的 Series
    print("replace()单个替换值:\n", seriesData.replace (11,99))
    print("replace()替换NaN空值:\n", seriesData.replace(np.nan, -1))
    # to_frame()	把一维的 Series 转成二维的 DataFrame
    print("to_frame()Series 变 DataFrame:\n",seriesData.to_frame(name="自定义列名：积分反馈"))


def doSeriesMethodV3():
    # equals()	判断两个 Series 是否完全一模一样（值、索引、顺序、空值都要一样）equals() 遇到 NaN 会认为相等
    s1 = pd.Series([11, 22, np.nan, 44, 22])
    s2 = pd.Series([11, 22, np.nan, 44, 22])
    print("equals()判断两个 Series 是否完全一模一样:\n", s1.equals(s2))

    # keys()	获取 Series 的索引（行号）
    print("keys()获取 Series 的索引（行号）:\n", seriesData.keys())
    print("keys()获取 Series 的索引（行号）和 .index 功能一致:\n", seriesData.index)
    print("*"*50)
    # corr() 计算两个 Series 之间的【相关系数】,两个 Series 长度必须一样,自动忽略 NaN（不会报错）
    # 说人话：看两个变量是不是 “一起变”，corr 看方向 + 强弱（最常用）它在 -1 到 1 之间，可比较
    # 相关系数是什么(范围：-1 ～ 1)
    # 默认使用皮尔逊相关系数（Pearson correlation coefficient）来计算相关性。
    # 参与比较的数组元素类型都是数值型。
    # 接近 -1：一涨一跌 → 负相关（你涨我跌）
    # 接近 0：没啥关系 → 无相关
    # 接近 1：同涨同跌 → 正相关
    # 案例计算相关系数
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([11, 22, 33, 44, 55])
    print("s1.corr(s2)计算接近 1：同涨同跌 → 正相关:\n", s1.corr(s2))
    s1 = pd.Series([1, 2, 3, 4, 5])    # s1 递增：1→2→3→4→5
    s2 = pd.Series([50, 40, 30, 20, 10])    # s2 递减：50→40→30→20→10
    print("s1.corr(s2)计算接近-1：一涨一跌 → 负相关（你涨我跌）:\n", s1.corr(s2))

    print("*"*50)
    # cov()协方差，计算两个 Series 的【协方差】，自动忽略空值，两个 Series 长度必须一样
    # 说人话：看两个变量变动方向是否一致cov只看方向，协方差大小没意义，只看正负号！
    # 【协方差】无范围（可正可负，可大可小），cov协方差只看正负号判断方向
    #正数：一起变大、一起变小（正相关）
    #负数：一个变大、一个变小（负相关）
    #0：不一起动
    # 案例说明，cov()  VS   corr() 对比见代码笔记最后
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([11, 22, 33, 44, 55])
    print("口诀：协方差看方向（±），相关系数看强弱（-1 到 1）")
    print("s1.cov(s2)协方差=27.5 > 0 → 正相关（同涨同跌）:\n", s1.cov(s2))
    print("corr()计算接近 1：同涨同跌 → 正相关:\n", s1.corr(s2))


    # hist()	绘制直方图，用于展示数据的分布情况。它将数据划分为若干个区间（也称为 “bins”）并统计每个区间内数据的频数。需要安装matplotlib包
    # bins=区间个数，默认是10，越多柱子越细,自动把你的数值范围平均切成10个柱子
    #数据少的时候，很多柱子会是空的（正常现象）数据多、分布广时，10个柱子刚好能看清分布
    seriesData.hist(bins=20)
    # 改颜色
    seriesData.hist(color='blue')
    # 横轴：数值区间 | 纵轴：每个区间里有多少个数据 |一眼看出：数据集中在哪个范围、有没有偏态
    plt.show()
    print("*"*50)
    # items()	循环拿每一行的 (索引，值),for 循环逐行读取 index 和 value
    # 循环遍历 index 和 value
    for index, value in seriesData.items():
        print(f"items()方法演示，索引：{index}，值：{value}")


if __name__ == '__main__':

    #doSeriesMethodV1()

    #doSeriesMethodV2()

    doSeriesMethodV3()




''' 对比总结
方法	    名字	        取值范围	                    作用
cov()	协方差	    无范围（可正可负，可大可小）	    看方向（同不同步）
corr()	相关系数	    -1 ~ 1	                    看方向 + 强度（标准化后的值）
'''