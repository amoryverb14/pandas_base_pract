'''
Created on May 2 14:02:00 2024

@author: amory
'''

import pandas as pd
import numpy as np
######第十一题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=2
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df}')
# # 添加新列
# # 自定义要添加的新列
# new_column = ['A', 'B', 'C', 'D']
# # 自定义要添加的新列的位置
# index_to_insert = 4
# # 使用insert方法在指定位置添加新列
# df.insert(loc=index_to_insert, column='新列', value=new_column)
# print(f'修改后表单\n{df}')


#####第十二题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name='收入'
# df=pd.read_excel(xlsx_flie,sheet_name=sheet_name)
# print(f'原本表单\n{df}')
# # 自定义要删除的列的索引
# index_to_drop = 7  # 假设要删除的
# # 使用drop方法删除指定索引的列
# df = df.drop(df.columns[index_to_drop], axis=1)
# print(f'修改后表单\n{df}')
# # 重新写入到Excel文件
# with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#     df.to_excel(writer, sheet_name=sheet_name, index=False)


#####第十三题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df}')
# df.loc[df['姓名'] == '李四', '地理'] = 45
# print("修改后的:")
# print(df)


######第十四题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df.head(9)}')
# # 提取性别为男的行
# male_df = df[df['性别'] == '男']
# print("性别为男的行：")
# print(male_df.head(9))
# # 提取数学成绩在55到60之间的男性行
# filtered_df = male_df[(male_df['数学'] >= 55) & (male_df['数学'] <= 60)]
# print("数学成绩在55到60之间的男性行:")
# print(filtered_df)


#######第十五题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df.head(9)}')
# # # 将李四的地理成绩改为NaN(这是设置空值,也可以用wps打开表格,随机删除几个也可以)
# df.loc[df['姓名'] == '李四', '地理'] = np.nan
# print("修改后的:")
# print(df.head(9))
# 删除包含空值的行
# df = df.dropna()
# print("删除空值后的")
# print(df)
# # 删除包含空值的列
# df = df.dropna(axis=1)
# print("删除空值后的:")
# print(df.head(9))

#####第十六题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df.head(9)}')
# # 提取包含空值的行
# null_rows = df[df.isna().any(axis=1)]
# print("包含空值的行：")
# print(null_rows)
# # 提取包含空值的列
# null_columns = df.columns[df.isna().any()]
# print("包含空值的列：")
# print(df[null_columns])


#######第十七题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=1
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df.head(9)}')
# # 统计得分在70到80之间的个数
# count = df[(df['得分'] >= 70) & (df['得分'] <= 80)].shape[0]
# print("得分在70到80之间的个数:", count)

#######第十八题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df.head(9)}')
# # 统计每个人数学、英语、物理、化学、历史、地理的总分
# df['总分'] = df[['数学', '英语', '物理', '化学', '历史', '地理']].sum(axis=1)
# print("每个人数学、英语、物理、化学、历史、地理的总分：")
# print(df.head(9))

#####第十九题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df.head(9)}')
# # 计算数学、英语、物理、化学、历史、地理的平均数，并添加到DataFrame最后一行
# average_row = df[['数学', '英语', '物理', '化学', '历史', '地理']].mean().round(1)
# average_row['姓名'] = '平均'
# average_row['性别'] = '无'
# df = df.append(average_row, ignore_index=True)
# print("数学、英语、物理、化学、历史、地理的平均数及最后一行：")
# print(df)

####第二十题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'原本表单\n{df.head(9)}')
# # 统计数学成绩在不同区间的人数
# math_bins = [0, 60, 70, 80, 90, 100]
# math_labels = ['0-60', '61-70', '71-80', '81-90', '91-100']
# df['数学区间'] = pd.cut(df['数学'], bins=math_bins, labels=math_labels)
# math_counts = df['数学区间'].value_counts().sort_index()
# print("数学成绩区间人数统计：")
# print(math_counts)