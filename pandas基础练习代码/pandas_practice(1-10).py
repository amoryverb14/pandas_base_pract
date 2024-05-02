'''
Created on Wednesday May 1 21:01:00 2024

@author: amory
'''

import pandas as pd
######第一题
# data1={
#     '姓名':['amory','amoryverb','张三','李四'],
#     '年龄':[22,22,19,24],
#     '月薪':[100000,100000,2,3]
# }
# df1=pd.DataFrame(data1)
# print(f'第一个表\n{df1}')
# data2=[
#     ['amory',100,100,99],
#     ['amoryverb',100,100,100],
#     ['张三',1,1,1]
# ]
# column=['姓名','语文','数学','英语']
# df2=pd.DataFrame(data2,columns=column)
# print(f'第二个表\n{df2}')
# write=pd.ExcelWriter('./data_practice/one.xlsx')
# df1.to_excel(write,sheet_name='收入表',index=False)
# df2.to_excel(write,sheet_name='成绩表',index=False)
# write.save()

#####第二题
# xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
# df1=pd.read_excel(xlsx_file,sheet_name=0)
# df2=pd.read_excel(xlsx_file,sheet_name='个人信息')
# df3=pd.read_excel(xlsx_file,sheet_name=2)
# print(f'第一个表单\n{df1.head(5)}\n第二个表单\n{df2.head(5)}\n第三个表单\n{df3.head(5)}\n')

######第三题
# ####方法一
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# df1=pd.read_excel(xlsx_flie,sheet_name=1)
# print(df1)
# df2=df1.loc[df1['姓名'].isin(['ammmory','钱七'])]
# df2=df2.to_string(header=False)
# print(df2)
# ####方法二
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# df1=pd.read_excel(xlsx_flie,sheet_name=1)
# # print(df1)
# df2=df1.iloc[[3,6]]
# df2=df2.to_string(header=False)
# print(df2)

#####第四题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# df=pd.read_excel(xlsx_flie,sheet_name=1)
# # print(df)
# ###方法一
# df2=df.iloc[3:7]    #左闭右开
# df2=df2.to_string(header=False)
# print(df2)
# ###方法二
# df3=df.loc[3:6]
# df3=df3.to_string(header=False)
# print(df3)

######第五题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# df=pd.read_excel(xlsx_flie,sheet_name=2)
# # print(df)
# ###方法一
# df2=df[['姓名','城市']]
# print(f'方法一\n{df2}\n')
# ###方法二
# df3=df.loc[:, ['姓名', '城市']]
# print(f'方法二\n{df3}\n')

######第六题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# df=pd.read_excel(xlsx_flie,sheet_name=2)
# df2=df.iloc[:,0:3]
# print(df2)

######第七题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# df=pd.read_excel(xlsx_flie,sheet_name=0)
# print(df)
# df2=df.iloc[3:6,0:3]
# df2=df2.to_string(header=False)
# print(df2)

#####第八题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# df=pd.read_excel(xlsx_flie,sheet_name=0)
# df_sorted = df.sort_values(by='数学', ascending=False)###Flase改成True就是升序
# print(df_sorted.head(5))
# df_sorted1 = df.sort_values(by='数学', ascending=True)###Flase改成True就是升序
# print(df_sorted1.head(5))

#####第九题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name='收入'
# df=pd.read_excel(xlsx_flie,sheet_name=sheet_name)
# print(df)
# # 新行的数据
# new_row_data = {'姓名': 'amory', '年龄': 22, '城市': '上海', '性别': '男', '工作': '吃牢饭', '月收入': 0, '收入来源': '无', '收入日期': '无'}
# # 指定要插入的索引位置
# insert_index = 2  # 在第2行（索引从0开始计数）插入新行数据
# # 在指定的索引位置插入新的行数据
# df = pd.concat([df.iloc[:insert_index], pd.DataFrame([new_row_data]), df.iloc[insert_index:]], ignore_index=True)
# # 写入到Excel文件
# with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#     df.to_excel(writer, sheet_name=sheet_name, index=False)


####第十题
# xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
# sheet_name='收入'
# df=pd.read_excel(xlsx_flie,sheet_name=sheet_name)
# #print(df)
# #####方法一
# # 使用标签 '姓名' 来删除行
# df = df.loc[df['姓名'] != 'amory']
# # 重新写入到Excel文件
# with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#     df.to_excel(writer, sheet_name=sheet_name, index=False)
# #####方法二,用索引,比如现在删除李四
# df = df.drop(1)
# # print(df)
# # 重新写入到Excel文件
# with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#     df.to_excel(writer, sheet_name=sheet_name, index=False)


