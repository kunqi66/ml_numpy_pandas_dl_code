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

# 1）数据连接的类型

# 1.1 数据连接的类型 一对一连接
def dataConnectionType1_1():
    df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                        "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    print(df1)
    df2 = pd.DataFrame({"employee": ["Lis", "Bob", "Jake", "Sue"],
                        "hire_date": [2004, 2008, 2012, 2014]})
    print(df2)

    # merge第一种使用方式 df1.merge(df2) 和 pd.merge(df1, df2) 完全一样
    print(df1.merge(df2))

    # merge第二种使用方式,家庭作业，自己看懂，O(∩_∩)O
    # merge 默认是 内连接（inner）= 一对一匹配,
    # pandas自动寻找两个表共有的列名employee然后按它连接，
    # 进行关联的一对一连接：一行 ↔ 一行，完全匹配，无空值
    #print("默认一对一内连接（只保留匹配）:\n",pd.merge(df1, df2))

# 1.2 数据连接的类型 一对N连接
# pd.merge(df1, df2) 不指定连接键时，自动取两张表同名列 group 作为关联条件，默认连接方式 how='inner'。
# 属于典型一对多关联：df2 一条部门 → 匹配 df1 多条员工。
# 一边重复，另一边不重复，一个部门一个主管，一个部门多个员工
def dataConnectionType1_N():
    df1 = pd.DataFrame(
        {"employee": ["Bob", "Jake", "Lisa", "Sue"],
         "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    print(df1)
    df2 = pd.DataFrame(
        {"group": ["Accounting", "Engineering", "HR"],
         "supervisor": ["Carly", "Guido", "Steve"]})
    print(df2)
    print(pd.merge(df1, df2)) #等价pd.merge(df1, df2, on="group")

# 1.3 数据连接的类型 多对多连接
# 如果左右两个输入的共同列都包含重复值，那么合并的结果就是一种多对多连接。
def dataConnectionTypeN_N():
    df1 = pd.DataFrame(
        {
            "employee": ["Bob", "Jake", "Lisa", "Sue"],
            "group": ["Accounting", "Engineering", "Engineering", "HR"]
         }
    )
    print("df1员工表:\n",df1)

    df2 = pd.DataFrame(
        {
            "group": ["Accounting", "Accounting", "Engineering", "Engineering", "HR", "HR"],
            "skills": ["math", "spreadsheets", "coding", "linux", "spreadsheets", "organization"],
        }
    )
    print("df2员工表:\n",df2)
    print()
    # 部门 → 员工：一对多
    # 1 个 Accounting 对应 Bob1 个人；
    # 1 个 Engineering 对应 Jake、Lisa 两个人；
    # 1 个 HR 对应 Sue1 个人
    # 部门 → 技能：一对多
    # 1 个 Accounting 有 math、spreadsheets 两项技能；
    # Engineering 有 coding、linux；
    # HR 两项技能
    # 两张表都靠 group 绑定，两张表各自对 group 都是一对多，
    # 合在一起表与表之间就变成多对多关系，匹配时触发笛卡尔乘积。
    '''
    乘积计算明细
    Accounting
    员工数：1 人，技能数：2 个 → 1×2 = 2 行
    Engineering
    员工数：2 人，技能数：2 个 → 2×2 = 4 行
    HR
    员工数：1 人，技能数：2 个 →1×2 = 2 行
    总条数：2+4+2 = 8 行
    '''
    print("多对多 merge 结果,左边一个组对应多行，右边同一个组也对应多行 →"
          " 两两匹配，产生笛卡尔积:\n",pd.merge(df1, df2))

# 2）设置合并的键与索引
# merge()会将两个输入的一个或多个共同列作为键进行合并。但由于两个输入要合并的列通常都不是同名的，
# 因此merge()提供了一些参数处理这个问题。

# 2.1 通过on指定使用某个列连接，只能在有共同列名的时候使用
def merge_On():
    df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                        "group": ["Accounting", "Engineering", "Engineering", "HR"]})
    df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"],
                        "hire_date": [2004, 2008, 2012, 2014]})
    #手动明确指定按 employee 列连接，它是之前讲解的1:1写法的手动版
    df3 = pd.merge(df1, df2, on="employee")
    print("手动明确指定按 employee 列连接，它是之前讲解的1:1写法的手动版:\n",df3)






# 2.2 两对象列名不同（employee（员工姓名）/name（也是员工姓名）），通过left_on和right_on分别指定列名
def merge_Lefton_Righton():
    df1 = pd.DataFrame({
         "employee": ["Bob", "Jake", "Lisa", "Sue"],
         "group": ["Accounting", "Engineering", "Engineering", "HR"]})

    df2 = pd.DataFrame({
            "name": ["Bob", "Jake", "Lisa", "Sue"],
            "salary": [70000, 80000, 120000, 90000]})

    # 关键：employee（员工姓名）/name（也是员工姓名）
    # 含义一样，但列名不一样，不能用 on="xxx"，必须用 left_on + right_on，两者 必须成对一起用，缺一不可
    # 效果：把 employee 和 name 按内容匹配,依然是 一对一连接
    df3 = pd.merge(df1, df2, left_on="employee", right_on="name")
    print("两对象列名不同，通过left_on和right_on分别指定列名:\n",df3)




# 2.3 通过left_index和right_index设置合并的索引
def merge_LeftIndex_RightIndex():
    df1 = pd.DataFrame(
        {"employee": ["Bob", "Jake", "Lisa", "Sue"],
         'test':[1,2,3,4],
         "group": ["Accounting", "Engineering", "Engineering", "HR"]}
    )
    df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"],
                        'test':[5,6,7,8],
                        "hire_date": [2004, 2008, 2012, 2014]})

    # 把 employee 这一列提升为行索引,原来的列消失，变成最左边的索引
    df1.set_index("employee", inplace=True)
    df2.set_index("employee", inplace=True)
    # left_index=True：用左边表的索引来匹配，right_index=True：用右边表的索引来匹配，两个必须同时写
    # 作用等价于：按索引列进行连接，依然是 一对一 1:1 连接
    df3 = pd.merge(df1, df2,left_index=True, right_index=True)
    print("按索引连接结果:\n",df3)

# DataFrame实现了join()方法，可以按照索引进行数据合并。
def myJoin():
    df1 = pd.DataFrame({
        'key': ['A', 'B', 'C'],
        'value1': [1, 2, 3]
    })
    df2 = pd.DataFrame({
        'key': ['B', 'C', 'A'],
        'value2': [4, 5, 6]
    })
    # ValueError: columns overlap but no suffix specified: Index(['key'], dtype='str')
    # df1 和 df2 都有同名列 key，.join()在合并时遇到重复列名，不知道怎么区分，又没给左右后缀，直接抛出异常。
    # 而 pd.merge 遇到重名列会自动给加上 _x、_y，所以不会报这个错。
    #print(df1.join(df2))
    #同名列key重复，必须指定左右后缀
    # join() 默认按【索引】+左连接（left）合并，当列名重复时必须加lsuffix和rsuffix
    # join () 默认是左连接（left join），以左表 df1 的索引为准，右表 df2 匹配不上的填 NaN
    print(df1.join(df2, lsuffix='_left', rsuffix='_right', how='left'))

# 3）设置数据连接的集合操作规则
# 3.1
# left 左连接：以左表为准，左边全留，右边匹配不上 → NaN
# right 右连接：以右表为准，右边全留，左边匹配不上 → NaN
# outer 外连接：所有人都留下，缺啥补啥 NaN
# inner 内连接：只留两边都有的
def connectionByHow():
    df1 = pd.DataFrame({
            "name": ["Peter", "Paul", "Mary"],
            "food": ["fish", "beans", "bread"]},columns=["name", "food"])
    print("===== 左表 df1 =====\n",df1)

    df2 = pd.DataFrame({
            "name": ["Mary", "Joseph"],
            "drink": ["wine", "beer"]}, columns=["name", "drink"])
    print("===== 右表 df2 =====\n",df2)

    print("左连接 how='left':\n",pd.merge(df1, df2, on="name", how="left"))
    print("右连接 how='right':\n",pd.merge(df1, df2, on="name", how="right"))
    print("外连接（保留所有人） how='outer':\n",pd.merge(df1, df2, on="name", how="outer"))
    print("inner内连接：只留两边都有的':\n",pd.merge(df1, df2, on="name", how="inner"))

# 4）重复列名的处理,家庭作业，自己看懂，O(∩_∩)O
# 4.1 可能会遇到两个输入DataFrame有重名列的情况:
# merge()会自动为其增加后缀_x和_y，也可以通过suffixes参数自定义后缀名。
def dealDuplicateColumn():
    df1 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [1, 2, 3, 4]})
    df2 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [3, 1, 4, 2]})

    print(pd.merge(df1, df2, on="name"))  # 不指定后缀名，默认为_x和_y
    print(pd.merge(df1, df2, on="name", suffixes=("_df1", "_df2")))  # 通过suffixes指定后缀名

if __name__ == '__main__':

    #dataConnectionType1_1()

    #dataConnectionType1_N()

    #dataConnectionTypeN_N()
    '''
    上面3种连接小总结：
    连接类型    特点  结果行数
    一对一     1:1	两边键都唯一	不变
    一对多     1:N	一边键重复	变多（复制 “一” 端）
    多对多     N:M	两边键都重复	乘积（笛卡尔积）
    '''
    print()
    # 2.1 通过on指定使用某个列连接，只能在有共同列名的时候使用
    #merge_On()

    #merge_Lefton_Righton()

    merge_LeftIndex_RightIndex()
    '''
    上面3种设置合并的键与索引
    一句话总结：
    列同名用 on，
    列不同用 left/right_on，
    索引用 left/right_index！
    '''
    print()
    myJoin()
    '''
    上面 merge VS join
    merge ：按 相同列名 连接+默认 内连接（inner），自动分配后缀
    join:   按 索引 连接+默认 左连接（left），重列要加后缀
    '''

    connectionByHow()

    # 家庭作业，自己看懂
    dealDuplicateColumn()