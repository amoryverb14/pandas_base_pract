```python
Created on Wednesday Apr 25 22:11:10 2024

@author: amory
```

# pandas_document

## 介绍


Pandas 是一个用于数据分析和处理的强大 Python 库。它提供了高效的数据结构和数据分析工具，使得在 Python 中进行数据清洗、准备、分析和可视化变得更加简单和快速。

下面是 Pandas 的一些主要特点和功能：

1. **数据结构：**
   - **Series：** 一维带标签的数组，类似于 Python 的字典和列表的混合体。
   - **DataFrame：** 二维的、大小可变的、表格型的数据结构，每列可以是不同的数据类型，类似于 Excel 表格或 SQL 表。
   - **Index：** 行或列的标签。
2. **数据输入/输出：**
   - Pandas 支持从各种文件格式（如 CSV、Excel、JSON、SQL、HTML 等）中读取数据，并能将数据写入到这些格式中。
3. **数据清洗和处理：**
   - 支持缺失值处理，包括填充、删除等操作。
   - 提供了丰富的数据转换和处理功能，如合并、拆分、过滤、排序、分组等。
   - 可以对数据进行重塑、透视和汇总操作。
4. **数据分析：**
   - 提供了统计函数和描述性统计分析工具，如平均值、中位数、标准差、相关系数等。
   - 支持数据透视表（Pivot Table）和交叉表（Cross Tabulation）等数据分析操作。
5. **数据可视化：**
   - 可以与 Matplotlib 等可视化库结合使用，快速绘制图表和图形，如折线图、柱状图、散点图等。

Pandas 的优势在于其灵活性、高效性和易用性，使得用户能够快速地对数据进行探索、分析和处理。它已成为数据科学和数据分析领域的重要工具之一，在数据清洗、预处理、建模和可视化等方面都发挥着重要作用。

## pandas 的基本数据结构

Pandas 提供了两种类型的类来处理数据：

1. [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)：保存任何类型数据的一维标记数组

   例如整数、字符串、Python 对象等。

2. [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)：一种二维数据结构，用于保存数据，例如二维数组或具有行和列的表格。

## pandas读取

### 读取csv

```python
df=pd.read_csv('./data_practice/student.csv')
print(df)
```

```python
输出:
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_practice.py
     姓名  语文  数学  英语
0    周十  94  56  97
1   郑十二  81  88  85
2    孙九  68  79  81
3    张三  96  91  78
```

### 读取Excel

```python
df=pd.read_excel('./data_practice/other.xlsx')
print(df)
```

```python
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_practice.py
   名称 结果
0  张三  正
1  李四  反
```

### 读取Excel中的第二个表

```python
df = pd.read_excel('./data_practice/other.xlsx', sheet_name=1)
print(df.head())
```

```python
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_practice.py
  名字  数字
0  A   1
1  B   2
2  C   3
```

## pandas写入

### 写入csv

```python
########字典格式写入
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [30, 25, 35, 28, 40],
    '城市': ['北京', '上海', '广州', '深圳', '成都'],
    '性别': ['男', '女', '男', '女', '男']
}
df = pd.DataFrame(data)
df.to_csv('./data_practice/output.csv', index=False, encoding='utf-8')
```

```python
#######列表格式写入
data = [
    ['张三', 30, '北京', '工程师'],
    ['李四', 25, '上海', '教师'],
    ['王五', 35, '广州', '医生'],
    ['赵六', 40, '深圳', '律师']
]
columns = ['姓名', '年龄', '城市', '职业']
df = pd.DataFrame(data, columns=columns)
df.to_csv('output.csv', index=False, encoding='utf-8')
```

```python
###########元组格式写入
data = [
    ('张三', 30, '北京', '工程师'),
    ('李四', 25, '上海', '教师'),
    ('王五', 35, '广州', '医生'),
    ('赵六', 40, '深圳', '律师')
]
columns = ['姓名', '年龄', '城市', '职业']
df = pd.DataFrame(data, columns=columns)
df.to_csv('output.csv', index=False, encoding='utf-8')
```

```python
##########numpy数组
data = np.array([
    ['张三', 30, '北京', '工程师'],
    ['李四', 25, '上海', '教师'],
    ['王五', 35, '广州', '医生'],
    ['赵六', 40, '深圳', '律师']
])
columns = ['姓名', '年龄', '城市', '职业']
df = pd.DataFrame(data, columns=columns)
df.to_csv('output.csv', index=False, encoding='utf-8')
```

### 写入Excel

```python
######其他类似
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [30, 25, 35, 40],
    '城市': ['北京', '上海', '广州', '深圳'],
    '职业': ['工程师', '教师', '医生', '律师']
}
df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False, encoding='utf-8')
```

### 写入Excel多个子表

```python
# 创建第一个数据表
data1 = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [30, 25, 35, 28],
    '城市': ['北京', '上海', '广州', '深圳'],
    '性别': ['男', '女', '男', '女'],
    '工作': ['工程师', '医生', '设计师', '教师'],
    '身高': [175, 163, 180, 168],
    '体重': [70, 55, 75, 60],
    '得分': [85, 92, 78, 88]
}
df1 = pd.DataFrame(data1)
# 创建第二个数据表
data2 = {
    '姓名': ['张三', '李四', '王五'],
    '性别': ['男', '女', '男'],
    '数学': [68, 60, 88],
    '英语': [64, 66, 58],
    '物理': [60, 70, 50],
    '化学': [91, 64, 70],
    '历史': [50, 54, 58],
    '地理': [58, 95, 66]
}
df2 = pd.DataFrame(data2)
# 创建一个Excel写入对象
writer = pd.ExcelWriter('./data_practice/test.xlsx')
# 将第一个数据表写入到第一个工作表中
df1.to_excel(writer, sheet_name='表1', index=False)
# 将第二个数据表写入到第二个工作表中
df2.to_excel(writer, sheet_name='表2', index=False)
# 保存Excel文件
writer.save()
```

第二个演示:

```python
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
writer = pd.ExcelWriter('./data_practice/pandas练习表.xlsx')
# 将第一个数据表写入到第一个工作表中
df.to_excel(writer, sheet_name='学生成绩', index=False)
# 将第二个数据表写入到第二个工作表中
df1.to_excel(writer, sheet_name='个人信息', index=False)
df1.to_excel(writer, sheet_name='收入', index=False)
# 保存Excel文件
writer.save()
```

## pandas切片

比如目前有一个csv文件,内容是:

```python
姓名,年龄,城市,性别 #0
张三,30,北京,男 #1
李四,25,上海,女 #2
王五,35,广州,男 #3
赵六,28,深圳,女 #4
钱七,40,成都,男 #5
```

### 读取行

比如我们需要读取以下内容:

```python
姓名,年龄,城市,性别 #0
张三,30,北京,男 #1
李四,25,上海,女 #2
王五,35,广州,男 #3
赵六,28,深圳,女 #4
```

#### 采用位置索引:(*左闭右开*)

```python
df=pd.read_csv('./data_practice/output.csv')
df=df.iloc[1:4]
```

`df.iloc[1:4]` 是 Pandas 中 DataFrame 的一种切片操作。在这个例子中，`iloc` 表示通过行的位置（integer location）来进行索引。

- `1` 表示选择索引为1的行，注意在 Python 中索引是从0开始的，所以实际选择的是第1行。
- 4 表示选择到索引为4的行，但不包括索引为4的行，所以实际上选择的是第2行到第4行（不包括第4行）。

#### 采用标签索引:

```python
df2=df.loc[df['姓名'].isin(['张三','李四', '王五','赵六'])]
print(df2)
```

如果只想读取(第一行不读取,原本第一行是默认读取)

```python
张三,30,北京,男 #1
李四,25,上海,女 #2
王五,35,广州,男 #3
赵六,28,深圳,女 #4
```

```python
df2=df.loc[df['姓名'].isin(['张三','李四', '王五','赵六'])]
df2=df2.to_string(header=False)
print(df2)
```

### 读取列

#### 标签索引:

比如想读取性别这一列

```python
df = df.loc[:, '性别']
print(df)
```

```python
###结果
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_practice.py
0    男
1    女
2    男
3    女
4    男
Name: 性别, dtype: object
```

`:（冒号）` 表示选择所有行。列索引或列标签可以是单个整数（位置索引）或单个字符串（列标签），也可以是整数或字符串的列表，用于同时选择多个列。

想把列标签加上:

```python
df = df.loc[:, '性别']
df = df.to_frame(name='性别')
print(df)
```

```python
####结果
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_practice.py
  性别
0  男
1  女
2  男
3  女
4  男
```

#### 位置索引:

前景提要:

咱们扩建一个csv,现在的csv内容:(咱们称这个csv叫:test_one.csv)

```python
姓名,年龄,城市,性别,工作,身高,体重,得分
张三,30,北京,男,工程师,175,70,85
李四,25,上海,女,医生,163,55,92
王五,35,广州,男,设计师,180,75,78
赵六,28,深圳,女,教师,168,60,88
钱七,40,成都,男,企业家,185,80,91
刘八,33,重庆,女,程序员,170,65,75
陈九,27,武汉,男,律师,178,72,83
周十,32,南京,女,音乐家,160,58,89
吴十一,38,杭州,男,演员,172,68,80
郑十二,29,苏州,女,记者,165,62,86
```

读取城市到身高的所有列

```python
df=df.iloc[:,2:6]
print(df)  #######此时变成左闭右开
```

```python
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_practice.py
   城市 性别   工作   身高
0  北京  男  工程师  175
1  上海  女   医生  163
2  广州  男  设计师  180
3  深圳  女   教师  168
4  成都  男  企业家  185
5  重庆  女  程序员  170
6  武汉  男   律师  178
7  南京  女  音乐家  160
8  杭州  男   演员  172
9  苏州  女   记者  165
```

### 交叉读取

1.现在咱们想读取以下内容:

```python
####4,5列,6,7行
女,程序员
男,律师
```

```python
#####','前是行,左开右闭
#####','后是列,左闭右开
df=df.iloc[5:7,3:5]
print(df)
```

```python
####结果
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_practice.py
  性别   工作
5  女  程序员
6  男   律师
```

2.现在咱们想读取以下内容:

```python
王五,男,设计师,180
赵六,女,教师,168
```

```python
# 这里的[2, 3]表示第3和第4行，[0, 3, 4, 5]表示第1、第4、第5、第6列
#','前减一,后加一
df=df.iloc[[2, 3], [0, 3, 4, 5]]  
print(df)
```

## pandas排序

现在有学生表,咱们看一下前8行

```python
   姓名 性别  数学  英语  物理  化学  历史  地理
0  张三  男  68  64  60  91  50  58
1  李四  女  60  66  70  64  54  95
2  王五  男  88  58  50  70  58  66
3  赵六  女  66  90  58  50  64  98
4  钱七  男  58  88  66  58  54  50
5  刘八  女  70  58  50  64  98  66
6  陈九  男  64  66  98  54  50  70
7  周十  女  66  70  64  98  66  58
```

咱们现在需要,按照数学成绩高低,从高到低(从低到高)排序:

```python
df_sorted = df.sort_values(by='数学', ascending=False)###Flase改成True就是升序
print(df_sorted.head(8))
```

```python
##结果
PS D:\xuexi\vscode_learning\vscode_python_amory\python_learning\python_data_analysis> & D:/xuexi/anaconda/envs/learning/python.exe d:/xuexi/vscode_learning/vscode_python_amory/python_learning/python_data_analysis/pandas_two.py
     姓名 性别  数学  英语  物理  化学  历史  地理
12  赵十五  男  98  58  50  64  58  66
2    王五  男  88  58  50  70  58  66
5    刘八  女  70  58  50  64  98  66
0    张三  男  68  64  60  91  50  58
7    周十  女  66  70  64  98  66  58
15  陈十八  女  66  64  58  50  54  98
9   郑十二  女  66  58  64  70  58  50
3    赵六  女  66  90  58  50  64  98
```

## pandas增删改

因为Excel支持多表单所以接下来全是Excel

### 增加行(多表单)

```python
# 读取Excel文件
excel_file = './data_practice/pandas练习表.xlsx'
# 读取第二个表单的数据
sheet_name = "个人信息"  # 修改为你第二个表单的名称
df = pd.read_excel(excel_file, sheet_name)
# 新行的数据
new_row_data = {'姓名': 'ammmory', '年龄': 25, '城市': '深圳', '性别': '女', '工作': '设计师', '身高': 168, '体重': 55, '得分': 90}
# 指定要插入的索引位置
insert_index = 2  # 在第2行（索引从0开始计数）插入新行数据
# 在指定的索引位置插入新的行数据
df = pd.concat([df.iloc[:insert_index], pd.DataFrame([new_row_data]), df.iloc[insert_index:]], ignore_index=True)
# 写入到Excel文件
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
```

### 增加行(单表单)

```python
# 读取 Excel 文件
excel_file = './data_practice/pandas练习表(单表单).xlsx'
df = pd.read_excel(excel_file)
# 新行的数据
new_row_data =  {'姓名': 'amory', '年龄': 32, '城市': '成都', '性别': '男', '工作': '程序员', '身高': 178, '体重': 72, '得分': 90}
# 确定要插入新行的行数，假设在第2行插入
insert_index = 2
# 将 DataFrame 分成两部分，然后在指定的索引位置插入新行
df = pd.concat([df.iloc[:insert_index], pd.DataFrame([new_row_data]), df.iloc[insert_index:]]).reset_index(drop=True)
# 保存回 Excel 文件
df.to_excel(excel_file, index=False) 
```

