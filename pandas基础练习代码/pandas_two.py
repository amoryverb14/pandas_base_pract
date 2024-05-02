import pandas as pd

# # 读取Excel文件
# excel_file = './data_practice/pandas练习表(多表单).xlsx'
# # 读取第二个表单的数据
# sheet_name = "个人信息"  # 修改为你第二个表单的名称
# df = pd.read_excel(excel_file, sheet_name)
# # 新行的数据
# new_row_data = {'姓名': 'amory', '年龄': 25, '城市': '深圳', '性别': '女', '工作': '设计师', '身高': 168, '体重': 55, '得分': 90}
# # 指定要插入的索引位置
# insert_index = 2  # 在第2行（索引从0开始计数）插入新行数据
# # 在指定的索引位置插入新的行数据
# df = pd.concat([df.iloc[:insert_index], pd.DataFrame([new_row_data]), df.iloc[insert_index:]], ignore_index=True)
# # 写入到Excel文件
# with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#     df.to_excel(writer, sheet_name=sheet_name, index=False)

# # 读取 Excel 文件
# excel_file = './data_practice/pandas练习表(单表单).xlsx'
# df = pd.read_excel(excel_file)
# # 新行的数据
# new_row_data =  {'姓名': 'amory', '年龄': 32, '城市': '成都', '性别': '男', '工作': '程序员', '身高': 178, '体重': 72, '得分': 90}
# # 确定要插入新行的行数，假设在第2行插入
# insert_index = 2
# # 将 DataFrame 分成两部分，然后在指定的索引位置插入新行
# df = pd.concat([df.iloc[:insert_index], pd.DataFrame([new_row_data]), df.iloc[insert_index:]]).reset_index(drop=True)
# # 保存回 Excel 文件
# df.to_excel(excel_file, index=False)  


