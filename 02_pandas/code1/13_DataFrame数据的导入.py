import os
import pandas as pd
from datetime import datetime

date_str = datetime.now().strftime("%Y%m%d")

df_csv = pd.read_csv(f"../data/df_{date_str}.csv",sep="\t")
print("读取csv数据并打印:\n",df_csv)

df_excel = pd.read_excel(f"../data/df_{date_str}.xlsx")
print("读取excel数据并打印:\n",df_excel)


df_json = pd.read_json(f"../data/df_{date_str}.json")
print("读取json数据并打印:\n",df_json)