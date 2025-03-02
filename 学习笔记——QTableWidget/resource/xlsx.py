# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME xlsx
AUTHOR Pfolg
TIME 2025/3/2 13:22
# pandas+numpy+matplotlib
"""
import pandas as pd

table = pd.read_excel("sample.xlsx", sheet_name="sheet1")
header = []
# 获取表头
for i in table:
    header.append(i)
# print(header)
np_table = table.to_numpy()
# print(np_table, header, len(np_table), len(np_table[0]))
print(*header)
for i in np_table:
    print(*i)
