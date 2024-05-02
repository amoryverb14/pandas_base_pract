'''
Created on May 2 15:30:00 2024

@author: amory
'''
import pandas as pd
##########第二十一题
# xlsx_file='./data_practice/拼接练习表.xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'表单一\n{df.head(5)}')
# sheet_name=1
# df2=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'表单二\n{df2.head(5)}')
# # 使用merge函数进行拼接，指定按照姓名和性别拼接
# merged_df = pd.merge(df, df2, on=['姓名', '性别'])
# print(f'拼接完成后\n{merged_df.head(5)}')

##########第二十二题
# xlsx_file='./data_practice/拼接练习表.xlsx'
# sheet_name=0
# df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'表单一\n{df.head(5)}')
# sheet_name=2
# df2=pd.read_excel(xlsx_file,sheet_name=sheet_name)
# print(f'表单二\n{df2.head(5)}')
# # 使用 concat() 函数将两个 DataFrame 沿着列方向拼接
# result = pd.concat([df, df2], ignore_index=True)
# print(f'拼接完成后\n{result}')