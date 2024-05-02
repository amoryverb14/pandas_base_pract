import pandas as pd
import numpy as np
########读取

# df=pd.read_csv('./data_practice/student.csv')
# df_sort=df.sort_values(by='英语',ascending=False).reset_index(drop=True)
# df_sort.to_csv('./data_practice/student.csv',index=False)
# print(df_sort)
# df=pd.read_csv('./data_practice/student.csv')
# print(df)
'''
# df=pd.read_excel('./data_practice/other.xlsx')
# print(df)
# df = pd.read_excel('./data_practice/other.xlsx', sheet_name=1)
# print(df.head())
'''

########写入

# data = {
#     '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
#     '年龄': [30, 25, 35, 28, 40],
#     '城市': ['北京', '上海', '广州', '深圳', '成都'],
#     '性别': ['男', '女', '男', '女', '男']
# }
# df = pd.DataFrame(data)
# df.to_csv('./data_practice/output.csv', index=False, encoding='utf-8')
# data = [
#     ['张三', 30, '北京', '工程师'],
#     ['李四', 25, '上海', '教师'],
#     ['王五', 35, '广州', '医生'],
#     ['赵六', 40, '深圳', '律师']
# ]
# columns = ['姓名', '年龄', '城市', '职业']
# df = pd.DataFrame(data, columns=columns)
# df.to_csv('output.csv', index=False, encoding='utf-8')
# data = [
#     ('张三', 30, '北京', '工程师'),
#     ('李四', 25, '上海', '教师'),
#     ('王五', 35, '广州', '医生'),
#     ('赵六', 40, '深圳', '律师')
# ]
# columns = ['姓名', '年龄', '城市', '职业']
# df = pd.DataFrame(data, columns=columns)
# df.to_csv('output.csv', index=False, encoding='utf-8')
# data = np.array([
#     ['张三', 30, '北京', '工程师'],
#     ['李四', 25, '上海', '教师'],
#     ['王五', 35, '广州', '医生'],
#     ['赵六', 40, '深圳', '律师']
# ])
# columns = ['姓名', '年龄', '城市', '职业']
# df = pd.DataFrame(data, columns=columns)
# df.to_csv('output.csv', index=False, encoding='utf-8')
# 创建第一个子表的数据

# data = {
#     '姓名': ['张三', '李四', '王五', '赵六'],
#     '年龄': [30, 25, 35, 40],
#     '城市': ['北京', '上海', '广州', '深圳'],
#     '职业': ['工程师', '教师', '医生', '律师']
# }
# df = pd.DataFrame(data)
# df.to_excel('output.xlsx', index=False, encoding='utf-8')
#df=pd.read_csv('./data_practice/output.csv')

# 创建第一个数据表
# data1 = {
#     '姓名': ['张三', '李四', '王五', '赵六'],
#     '年龄': [30, 25, 35, 28],
#     '城市': ['北京', '上海', '广州', '深圳'],
#     '性别': ['男', '女', '男', '女'],
#     '工作': ['工程师', '医生', '设计师', '教师'],
#     '身高': [175, 163, 180, 168],
#     '体重': [70, 55, 75, 60],
#     '得分': [85, 92, 78, 88]
# }
# df1 = pd.DataFrame(data1)
# # 创建第二个数据表
# data2 = {
#     '姓名': ['张三', '李四', '王五'],
#     '性别': ['男', '女', '男'],
#     '数学': [68, 60, 88],
#     '英语': [64, 66, 58],
#     '物理': [60, 70, 50],
#     '化学': [91, 64, 70],
#     '历史': [50, 54, 58],
#     '地理': [58, 95, 66]
# }
# df2 = pd.DataFrame(data2)
# # 创建一个Excel写入对象
# writer = pd.ExcelWriter('./data_practice/test.xlsx')
# # 将第一个数据表写入到第一个工作表中
# df1.to_excel(writer, sheet_name='表1', index=False)
# # 将第二个数据表写入到第二个工作表中
# df2.to_excel(writer, sheet_name='表2', index=False)
# # 保存Excel文件
# writer.save()


# 创建数据
data = {
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "刘八", "陈九", "周十", "吴十一", "郑十二",
           "李十三", "王十四", "赵十五", "钱十六", "刘十七", "陈十八", "周十九", "吴二十"],
    "性别": ["男", "女", "男", "女", "男", "女", "男", "女", "男", "女",
           "男", "女", "男", "女", "男", "女", "男", "女"],
    "数学": [68, 60, 88, 66, 58, 70, 64, 66, 58, 66,
           64, 58, 98, 58, 64, 66, 58, 66],
    "英语": [64, 66, 58, 90, 88, 58, 66, 70, 95, 58,
           66, 64, 58, 98, 58, 64, 66, 58],
    "物理": [60, 70, 50, 58, 66, 50, 98, 64, 50, 64,
           58, 66, 50, 70, 66, 58, 50, 98],
    "化学": [91, 64, 70, 50, 58, 64, 54, 98, 54, 70,
           50, 58, 64, 58, 98, 50, 58, 66],
    "历史": [50, 54, 58, 64, 54, 98, 50, 66, 58, 58,
           95, 50, 58, 66, 58, 54, 70, 58],
    "地理": [58, 95, 66, 98, 50, 66, 70, 58, 66, 50,
           58, 54, 66, 64, 50, 98, 64, 50]
}
data1 = {
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "刘八", "陈九", "周十", "吴十一", "郑十二"],
    "年龄": [30, 25, 35, 28, 40, 33, 27, 32, 38, 29],
    "城市": ["北京", "上海", "广州", "深圳", "成都", "重庆", "武汉", "南京", "杭州", "苏州"],
    "性别": ["男", "女", "男", "女", "男", "女", "男", "女", "男", "女"],
    "工作": ["工程师", "医生", "设计师", "教师", "企业家", "程序员", "律师", "音乐家", "演员", "记者"],
    "身高": [175, 163, 180, 168, 185, 170, 178, 160, 172, 165],
    "体重": [70, 55, 75, 60, 80, 65, 72, 58, 68, 62],
    "得分": [85, 92, 78, 88, 91, 75, 83, 89, 80, 86]
}
# 创建数据
data2 = {
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "年龄": [30, 25, 35, 28, 40],
    "城市": ["北京", "上海", "广州", "深圳", "成都"],
    "性别": ["男", "女", "男", "女", "男"],
    "工作": ["工程师", "医生", "设计师", "教师", "企业家"],
    "月收入": [10000, 12000, 8000, 15000, 20000],
    "收入来源": ["工资", "工资", "兼职", "工资", "投资"],
    "收入日期": ["2024-04-01", "2024-04-05", "2024-04-10", "2024-04-15", "2024-04-20"]
}
# 创建DataFrame
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
df2=pd.DataFrame(data2)
# 创建一个Excel写入对象
writer = pd.ExcelWriter('./data_practice/pandas练习表(多表单).xlsx')
# 将第一个数据表写入到第一个工作表中
df.to_excel(writer, sheet_name='学生成绩', index=False)
# 将第二个数据表写入到第二个工作表中
df1.to_excel(writer, sheet_name='个人信息', index=False)

df2.to_excel(writer, sheet_name='收入', index=False)
# 保存Excel文件
writer.save()

#######切片
# df=df.iloc[0:4]
# df=df.to_string(header=False)
# print(df)

# df2=df.loc[df['姓名'].isin(['张三','李四', '王五','赵六'])]
# df2=df2.to_string(header=False)
# print(df2)
# df = df.loc[:, '性别']
# df = df.to_frame(name='性别')
# print(df)
# df=df.iloc[:,2:6]
# print(df)
# df=df.iloc[5:7,3:5]
# print(df)

# # 使用iloc根据行索引位置筛选数据
# filtered_data = df.iloc[[2, 3], [1, 4]]  # 这里的[2, 3]表示第3和第4行，[1, 4]表示第2和第5列

# # 显示筛选后的数据
# print(filtered_data)
# df=df.iloc[[2, 3], [0, 3, 4, 5]]  # 这里的[2, 3]表示第3和第4行，[0, 3, 4, 5]表示第1、第4、第5、第6列
# print(df)


