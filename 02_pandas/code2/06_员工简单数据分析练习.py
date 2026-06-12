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

# 1 读取员工数据
df = pd.read_csv("../data/employees.csv")
#print("员工信息初始数据：\n",df)
#
# #使用employees（员工）数据集，其中包含10个字段类型等说明：
# #print(df.info())
#
# # 2 查看统计信息
print("describe()方法查看统计信息:\n",df.describe())
print("shape属性查看数据形状(多少行row，多少列column):\n",df.shape)
#
# 3）找出薪资最低、最高的员工
print("最低薪资的员工:\n",df[df["salary"] == df["salary"].min()])  # 找出最低薪资的员工
print("最低薪资的员工v2:\n",df.loc[df["salary"] == df["salary"].min()])  # 找出最低薪资的员工
# df.loc[ 条件 ] 把所有满足条件（工资 = 最高）的整行数据都找出来
print("最高薪资的员工:\n",df.loc[df["salary"] == df["salary"].max()])  # 找出最高薪资的员工
# # 家庭作业，自己思考懂......
print(df.sort_values("salary").head(1))  # 使用排序的方法找出最低薪资的员工
# # print(df.sort_values("salary", ascending=False).head(1))  # 使用排序的方法找出最高薪资的员工
#
# 4）找出薪资最高的10名员工
print("薪资最高的10名员工:\n",df.nlargest(10, "salary"))  # 薪资最高的10名员工

# 5）查看所有部门id 对标SELECT DISTINCT department_id FROM employees;
print("查看所有部门id，unique() = 去重:\n",df["department_id"].unique())
#
# 6）查看每个部门的员工数，对标mysql如下：
'''
SELECT
  department_id,
  COUNT(employee_id) AS employee_count  -- 这里 AS = pandas 的 rename
FROM employees
GROUP BY department_id;
'''
print("查看每个部门的员工数:\n",
      df.groupby("department_id")["employee_id"].count().rename("employee_count员工数量"))

# 7）绘图
df.groupby("department_id")["employee_id"].count().rename("employee_count").plot(kind="bar")
#显示图表
plt.show()

# 家庭作业，自己思考懂......
# 8）薪资的分布
# print(df["salary"].mean())  # 平均值
# print(df["salary"].std())  # 标准差
# print(df["salary"].median())  # 中位数
# 9）找出平均薪资最高的部门id
# print(df.groupby("department_id")["salary"].mean().nlargest(1))  # 平均薪资最高的部门
