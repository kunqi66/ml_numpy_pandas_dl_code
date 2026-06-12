from datetime import datetime
import os
import pandas as pd

#  exist_ok=True
#   文件夹不存在 → 正常创建文件夹
#   文件夹已存在 → 不报错、不覆盖、什么都不做，静默跳过
print("当前代码所在平级目录",os.makedirs("data2", exist_ok=True))


df = pd.DataFrame(data={"id": [101, 102, 103, 104],"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"]})
print(df)
df.set_index("id", inplace=True)
print(df)

date_str = datetime.now().strftime("%Y%m%d")

# to_csv
# index=False   不保存行索引(CSV 自带了行索引（0,1,2,3）)
# sep="\t"      设置分隔符为 \t
df.to_csv(f"../data/df_{date_str}.csv", index=True,sep="\t",encoding="utf-8")

# to_excel()	保存为Excel文件
# 需使用Conda安装openpyxl包。
df.to_excel(f"../data/df_{date_str}.xlsx")

# 保存为JSON格式,人话版推荐
# force_ascii=False    保留原始中文不转义,张三 就是 张三，不会变成 \u5f20\u4e09
# orient="records"     推荐格式：每行一条对象，最易读
# indent=4            格式化排版，好看
df = df.reset_index()
df.to_json(f"../data/df_{date_str}.json", force_ascii=False,orient="records",indent=4)