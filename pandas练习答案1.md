# pandas基础练习答案

题目涉及的文件在./data_practice/pandas练习表(多表单).xlsx

## 1. 新建一个Excel文件,且包含两个表单

```python
data1={
    '姓名':['amory','amoryverb','张三','李四'],
    '年龄':[22,22,19,24],
    '月薪':[100000,100000,2,3]
}
df1=pd.DataFrame(data1)
print(f'第一个表\n{df1}')
data2=[
    ['amory',100,100,99],
    ['amoryverb',100,100,100],
    ['张三',1,1,1]
]
column=['姓名','语文','数学','英语']
df2=pd.DataFrame(data2,columns=column)
print(f'第二个表\n{df2}')
write=pd.ExcelWriter('./data_practice/one.xlsx')
df1.to_excel(write,sheet_name='收入表',index=False)
df2.to_excel(write,sheet_name='成绩表',index=False)
write.save()
```

## 2. 分别读取Excel的三个表单

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
df1=pd.read_excel(xlsx_file,sheet_name=0)
df2=pd.read_excel(xlsx_file,sheet_name='个人信息')
df3=pd.read_excel(xlsx_file,sheet_name=2)
print(f'第一个表单\n{df1.head(5)}\n第二个表单\n{df2.head(5)}\n第三个表单\n{df3.head(5)}\n')
```

## 3. 读取第二个表单指定行

```python
####方法一
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
df1=pd.read_excel(xlsx_flie,sheet_name=1)
# print(df1)
df2=df1.loc[df1['姓名'].isin(['ammmory','钱七'])]
df2=df2.to_string(header=False)
print(df2)
```

```python
####方法二
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
df1=pd.read_excel(xlsx_flie,sheet_name=1)
# print(df1)
df2=df1.iloc[[3,6]]
df2=df2.to_string(header=False)
print(df2)
```

## 4. 读取第二个表单指定行区间

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
df=pd.read_excel(xlsx_flie,sheet_name=1)
# print(df)
###方法一
df2=df.iloc[3:7]    #左闭右开
df2=df2.to_string(header=False)
print(df2)
###方法二
df3=df.loc[3:6]
df3=df3.to_string(header=False)
print(df3)
```

## 5. 读取第三个表单指定列

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
df=pd.read_excel(xlsx_flie,sheet_name=2)
# print(df)
###方法一
df2=df[['姓名','城市']]
print(f'方法一\n{df2}\n')
###方法二
df3=df.loc[:, ['姓名', '城市']]
print(f'方法二\n{df3}\n')
```

## 6. 读取第三个表单指定列区间

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
df=pd.read_excel(xlsx_flie,sheet_name=2)
df2=df.iloc[:,0:3]
print(df2)
```

## 7. 读取第一个表单指定行列区间

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
df=pd.read_excel(xlsx_flie,sheet_name=0)
print(df)
df2=df.iloc[3:6,0:3]
df2=df2.to_string(header=False)
print(df2)
```

## 8. 升降序

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
df=pd.read_excel(xlsx_flie,sheet_name=0)
df_sorted = df.sort_values(by='数学', ascending=False)###Flase改成True就是升序
print(df_sorted.head(5))
df_sorted1 = df.sort_values(by='数学', ascending=True)###Flase改成True就是升序
print(df_sorted1.head(5))
```

## 9. 增加行

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
sheet_name='收入'
df=pd.read_excel(xlsx_flie,sheet_name=sheet_name)
print(df)
# 新行的数据
new_row_data = {'姓名': 'amory', '年龄': 22, '城市': '上海', '性别': '男', '工作': '吃牢饭', '月收入': 0, '收入来源': '无', '收入日期': '无'}
# 指定要插入的索引位置
insert_index = 2  # 在第2行（索引从0开始计数）插入新行数据
# 在指定的索引位置插入新的行数据
df = pd.concat([df.iloc[:insert_index], pd.DataFrame([new_row_data]), df.iloc[insert_index:]], ignore_index=True)
# 写入到Excel文件
with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
```

## 10. 删除行

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
sheet_name='收入'
df=pd.read_excel(xlsx_flie,sheet_name=sheet_name)
#print(df)
#####方法一
# 使用标签 '姓名' 来删除行
df = df.loc[df['姓名'] != 'amory']
# 重新写入到Excel文件
with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
#####方法二,用索引,比如现在删除李四
df = df.drop(1)
# print(df)
# 重新写入到Excel文件
with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
```

```python
让我逐步解释一下代码：

with pd.ExcelWriter(xlsx_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:：这行代码创建了一个 ExcelWriter 对象，它负责写入 Excel 文件。xlsx_file 是 Excel 文件的路径。engine='openpyxl' 表示使用 Openpyxl 引擎来操作 Excel 文件。mode='a' 表示以追加模式打开 Excel 文件，如果文件不存在则会创建。if_sheet_exists='replace' 表示如果要写入的工作表已经存在，则替换该工作表。
df.to_excel(writer, sheet_name=sheet_name, index=False)：这行代码将 DataFrame 写入到 Excel 文件中。writer 是 ExcelWriter 对象，sheet_name=sheet_name 指定要写入的工作表名称，index=False 表示不包含索引列。
```

## 11.增加列

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=2
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(df)
# 添加新列
# 自定义要添加的新列
new_column = ['A', 'B', 'C', 'D']
# 自定义要添加的新列的位置
index_to_insert = 4
# 使用insert方法在指定位置添加新列
df.insert(loc=index_to_insert, column='新列', value=new_column)
print(df)
```

## 12.删除列

```python
xlsx_flie='./data_practice/pandas练习表(多表单).xlsx'
sheet_name='收入'
df=pd.read_excel(xlsx_flie,sheet_name=sheet_name)
print(f'原本表单\n{df}')
# 自定义要删除的列的索引
index_to_drop = 7  # 假设要删除的
# 使用drop方法删除指定索引的列
df = df.drop(df.columns[index_to_drop], axis=1)
print(f'修改后表单\n{df}')
# 重新写入到Excel文件
with pd.ExcelWriter(xlsx_flie, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
```

## 13.改数据

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df}')
df.loc[df['姓名'] == '李四', '地理'] = 45
print("修改后的:")
print(df)
```

## 14.提取满足条件的行

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df.head(9)}')
# 提取性别为男的行
male_df = df[df['性别'] == '男']
print("性别为男的行：")
print(male_df.head(9))
# 提取数学成绩在55到60之间的男性行
filtered_df = male_df[(male_df['数学'] >= 55) & (male_df['数学'] <= 60)]
print("数学成绩在55到60之间的男性行:")
print(filtered_df)
```

## 15.过滤掉空值

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df.head(9)}')
# # 将李四的地理成绩改为NaN(这是设置空值,也可以用wps打开表格,随机删除几个也可以)
df.loc[df['姓名'] == '李四', '地理'] = np.nan
print("修改后的:")
print(df.head(9))
删除包含空值的行
df = df.dropna()
print("删除空值后的")
print(df)
# 删除包含空值的列
df = df.dropna(axis=1)
print("删除空值后的:")
print(df.head(9))
```

## 16.提取空值

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df.head(9)}')
# 提取包含空值的行
null_rows = df[df.isna().any(axis=1)]
print("包含空值的行：")
print(null_rows)
# 提取包含空值的列
null_columns = df.columns[df.isna().any()]
print("包含空值的列：")
print(df[null_columns])
```

## 17.统计满足条件的个数

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=1
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df.head(9)}')
# 统计得分在70到80之间的个数
count = df[(df['得分'] >= 70) & (df['得分'] <= 80)].shape[0]
print("得分在70到80之间的个数:", count)
```

## 18.统计总数

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df.head(9)}')
# 统计每个人数学、英语、物理、化学、历史、地理的总分
df['总分'] = df[['数学', '英语', '物理', '化学', '历史', '地理']].sum(axis=1)
print("每个人数学、英语、物理、化学、历史、地理的总分：")
print(df.head(9))
```

## 19.统计平均数

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df.head(9)}')
# 计算数学、英语、物理、化学、历史、地理的平均数，并添加到DataFrame最后一行
average_row = df[['数学', '英语', '物理', '化学', '历史', '地理']].mean().round(1)
average_row['姓名'] = '平均'
average_row['性别'] = '无'
df = df.append(average_row, ignore_index=True)
print("数学、英语、物理、化学、历史、地理的平均数及最后一行：")
print(df)
```

## 20.统计满足区间的个数

```python
xlsx_file='./data_practice/pandas练习表(多表单).xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'原本表单\n{df.head(9)}')
# 统计数学成绩在不同区间的人数
math_bins = [0, 60, 70, 80, 90, 100]
math_labels = ['0-60', '61-70', '71-80', '81-90', '91-100']
df['数学区间'] = pd.cut(df['数学'], bins=math_bins, labels=math_labels)
math_counts = df['数学区间'].value_counts().sort_index()
print("数学成绩区间人数统计：")
print(math_counts)
```

## 21.拼接两个表单

```python
xlsx_file='./data_practice/拼接练习表.xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'表单一\n{df.head(5)}')
sheet_name=1
df2=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'表单二\n{df2.head(5)}')
# 使用merge函数进行拼接，指定按照姓名和性别拼接
merged_df = pd.merge(df, df2, on=['姓名', '性别'])
print(f'拼接完成后\n{merged_df.head(5)}')
```

```python
pd.merge() 是 Pandas 库中用于合并（merge）两个 DataFrame 的函数。它提供了类似于 SQL 数据库连接操作的功能。以下是一些关键参数和用法：

参数说明：
left：要合并的左侧 DataFrame。
right：要合并的右侧 DataFrame。
how：指定合并方式，可以是 'inner'（内连接）、'outer'（外连接）、'left'（左连接）或 'right'（右连接）。
on：指定用于连接的列名。如果两个 DataFrame 的列名不同，可以分别指定 left_on 和 right_on。
left_on：左侧 DataFrame 用于连接的列名。
right_on：右侧 DataFrame 用于连接的列名。
suffixes：指定用于重叠列名的后缀，默认为 ('_x', '_y')。
合并方式：
内连接（inner）：只保留两个 DataFrame 中都有的行。
外连接（outer）：保留两个 DataFrame 中所有的行，缺失值填充为 NaN。
左连接（left）：以左侧 DataFrame 的行为基准，保留右侧 DataFrame 中与左侧匹配的行，缺失值填充为 NaN。
右连接（right）：以右侧 DataFrame 的行为基准，保留左侧 DataFrame 中与右侧匹配的行，缺失值填充为 NaN。
```

## 22.拼接两个表单(见题目描述)

```python
xlsx_file='./data_practice/拼接练习表.xlsx'
sheet_name=0
df=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'表单一\n{df.head(5)}')
sheet_name=2
df2=pd.read_excel(xlsx_file,sheet_name=sheet_name)
print(f'表单二\n{df2.head(5)}')
# 使用 concat() 函数将两个 DataFrame 沿着列方向拼接
result = pd.concat([df, df2], ignore_index=True)
print(f'拼接完成后\n{result}')
```

