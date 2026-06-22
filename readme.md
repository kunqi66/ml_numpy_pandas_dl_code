# 自学笔记 —— Python · SQL · NumPy · Pandas · Matplotlib · 机器学习

个人学习仓库，按技术栈分模块整理，从 Python 基础到机器学习算法逐步递进。

---

## 目录结构

```
.
├── 01_python_basic/        Python 基础（第1~13章）
├── 02_sql_exsice/          SQL 练习（MySQL，ch1~ch11）
├── 03_shell/               Shell 脚本
├── 04_numpy/               NumPy 学习
├── 05_pandas/              Pandas + Matplotlib 学习
├── 06_ml/                  机器学习算法
├── 99_self_leetcode/       LeetCode 刷题
└── data/                   公共数据集
```

---

## 各模块说明

### 01_python_basic — Python 基础

按章节组织，覆盖从语法入门到高级特性：

| 章节 | 内容 |
|------|------|
| 第3章 | 字面量、变量、数据类型、运算符、输入输出 |
| 第4章 | 条件分支、while / for 循环、嵌套循环 |
| 第5章 | 函数定义、参数类型、递归、作用域 |
| 第6章 | 列表、元组、字符串、集合、字典、切片 |
| 第7章 | 面向对象：类、继承、多态、魔法方法、抽象类 |
| 第8章 | 高阶函数、lambda、map/filter、推导式、闭包、装饰器、类型注解 |
| 第9章 | 异常处理、自定义异常 |
| 第10章 | 模块、标准库、包 |
| 第11章 | 迭代器、生成器 |
| 第12章 | 文件读写、目录操作 |
| 第13章 | 多进程、多线程、GIL 锁、进程池/线程池 |

---

### 02_sql_exsice — SQL 练习（MySQL）

> 该目录是独立的 git 仓库。

| 目录 | 内容 |
|------|------|
| ch1基本演示 | CREATE DATABASE / TABLE、INSERT、SELECT |
| ch2数据类型 | 整数、小数、字符串、日期类型 |
| ch3运算符 | 算术、比较、逻辑、模糊运算符 |
| ch4函数 | 单行函数（字符串/数学/日期/条件）、聚合函数 |
| ch5 | INSERT / UPDATE / DELETE / TRUNCATE |
| ch6 | 多表关联查询（七种 JOIN）、自连接、UNION |
| ch7 | SELECT 完整语法、GROUP BY、HAVING、ORDER BY、LIMIT 分页 |
| ch8 | 子查询（WHERE / SELECT / FROM / EXISTS） |
| ch9 | 约束（NOT NULL、UNIQUE、PRIMARY KEY、FOREIGN KEY、DEFAULT、CHECK） |
| ch10 | ALTER TABLE 修改表结构 |
| ch11 | 事务（ACID）、用户管理、窗口函数、CTE |
| **SQL学习笔记.md** | **完整学习笔记，含速查表和常见陷阱** |

---

### 04_numpy — NumPy

| 路径 | 内容 |
|------|------|
| `numpy_tutorial.ipynb` | **完整教程**（13章 + 附录速查表） |
| `ch1_ndarray/` | ndarray 属性与创建 |
| `ch2_ndarray_method/` | ndarray 方法详解 |
| `ch3_practice/` | 综合练习 |
| `code/` | 各知识点独立脚本（01~13） |

**教程内容：** ndarray 创建 → dtype → 索引切片（视图/副本陷阱）→ 形状操作 → ufunc → 广播 → 统计函数 → 排序搜索 → 线性代数 → 随机数 → 文件 I/O → 性能优化 → 综合实战（图像处理 + 蒙特卡洛）

---

### 05_pandas — Pandas & Matplotlib

| 路径 | 内容 |
|------|------|
| `pandas_beginner.ipynb` | **Pandas 完整教程**（13章 + 附录） |
| `matplotlib_tutorial.ipynb` | **Matplotlib 完整教程**（16章 + 附录） |
| `ch1_series/` | Series 基础 |
| `ch2_dataFrame/` | DataFrame 基础 |
| `ch3_dataanalysis/` | 数据分析实战 |
| `code1/` | Pandas 各知识点脚本（02~14） |
| `code2/` | 数据分析进阶脚本（01~08） |

**Pandas 教程内容：** Series/DataFrame → 索引（loc/iloc）→ 读写文件 → 缺失值/重复值处理 → 数据变换 → 分组聚合 → 数据合并（concat/merge）→ 时间序列 → 字符串操作 → 可视化 → 综合案例

**Matplotlib 教程内容：** pyplot vs OO API → Figure/Axes 层次 → 折线/散点/柱状/直方/饼图/箱线/小提琴/热力图/3D → GridSpec/subplot_mosaic → 文字注释 → 双轴/填充 → 色彩映射 → 样式配置 → 综合 Dashboard

---

### 06_ml — 机器学习

#### couser/ — 算法理论笔记（Jupyter Notebook）

| 文件 | 内容 |
|------|------|
| `math.ipynb` | 数学基础（线代、概率、微积分） |
| `ml_basic.ipynb` | 机器学习概述、sklearn 基础流程 |
| `lr.ipynb` | 线性回归 |
| `l_tree.ipynb` | 决策树 |
| `random_forest.ipynb` | 随机森林（Bagging、OOB、特征重要性） |
| `svm.ipynb` | 支持向量机 |
| `perceptron.ipynb` | 感知机（原始形式 + 对偶形式） |
| `cluster.ipynb` | 聚类算法 |
| `rl.ipynb` | 强化学习 |

#### recurrence_github/ — 算法手写复现

| 目录 | 内容 |
|------|------|
| `Liner_Regression/` | 手写线性回归 |
| `k-nearest_neighbor_algorithm/` | 手写 KNN |

#### 其他

- `beijing_weather.py` + `beijing_weather_202605.csv`：北京天气数据分析实战

---

### 99_self_leetcode — LeetCode 刷题

| 目录 | 内容 |
|------|------|
| `chapter1/` | 数据结构基础 + 笔记（数据结构.md） |
| `chapter2/` | 算法题练习 |
| `exercise/线性表/` | 线性表专题 |
| `exercise/树/` | 树专题 |

---

### data/ — 公共数据集

| 文件 | 说明 |
|------|------|
| `advertising.csv` | 广告投放与销售额 |
| `employees.csv` | 员工信息 |
| `heart_disease.csv` | 心脏病预测数据集 |
| `house_sales.csv` | 房屋销售数据 |
| `penguins.csv` | 企鹅分类数据集 |
| `sleep.csv` | 睡眠质量数据 |
| `weather.csv / weather_withna.csv` | 天气数据（含缺失值版本） |
| `train.csv` | 通用训练集 |

---

## 学习路线建议

```
Python 基础（01）
    ↓
SQL 入门（02）
    ↓
NumPy（04）→ Pandas + Matplotlib（05）
    ↓
机器学习数学基础 → 算法理论（06/couser）→ 手写复现（06/recurrence_github）
    ↓
LeetCode 数据结构与算法（99）
```

- **快速上手 NumPy/Pandas**：直接看 `04_numpy/numpy_tutorial.ipynb` 和 `05_pandas/pandas_beginner.ipynb`，也可只看 `code/` 目录下的独立脚本
- **SQL 完整复习**：查阅 `02_sql_exsice/SQL学习笔记.md`
- **机器学习算法**：先看 `math.ipynb` → `ml_basic.ipynb`，再按需阅读各算法 notebook
