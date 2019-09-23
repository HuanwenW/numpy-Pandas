import numpy as np

# ------代码学习知识点及代码示例------ #
""""
numpy基础运算：

(1)  np.arange() : 函数返回一个有终点和起点的固定步长的排列,3种参数情况用法
    如果要 同时 输出多个变量结果 ,变量中间使用逗号隔开,且引用变量为 % (变量1,变量2,变量3)
(2)  + - *  **2:数组的 加法、减法、乘法、平方(用2个*）、sin、cos 等数学函数用法 

(3)  random() : 随机生成数组  二维 多维 ,数值的大小范围 0-1之间的随机数

(4)  axis = 0/1: = 0时，将以 列 为查找单位 ； = 1，以 行 为单位查找

(5)  元素对应的索引 argmax/argmin:最大/小元素对应的索引

(6)  np.cumsum():累加函数:生成的每一项矩阵元素均是从原矩阵首项累加到对应项的元素之和
     np.diff():  每一行中后一项与前一项之差,得到的结果相比原矩阵将少一列
     
(7)  矩阵的2中转置方法

(8) np.clip(Array，Array_min,Array_max):将举证中> Array_max的替换成Array_max，<Array_min的替换成Array_min
"""
# (1)  np.arange() 函数分为 1个参数，2个参数，3个参数三种情况 及 同时输出多个变量书写规范

a1 = np.arange(4)     # 一个参数时，参数值为终点，起点取默认值0，步长取默认值1。
a2 = np.arange(2,6)   # 两个参数时，第一个参数为起点，第二个参数为终点，步长取默认值1。
a3 = np.arange(1,5,2) # 三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长。其中步长支持小数

print("a1:%s\na2:%s\na3:%s"%(a1,a2,a3)) # 同时输出3个变量查看结果
print('***'*15)

# （2）数组的 + - * **2 sin cos  等函数运算
b = np.array([0,2,6,9])
print("b:%s\na1+b:%s\na1-b:%s\na1*b:%s\nb**2:%s"%(b,a1+b,a1-b,a1*b, b**2))
print(10*np.sin(b))

print('***'*15)

# 二维数组及多维数组的运算
a4 = np.arange(4).reshape((2,2)) # !reshape() 对数组的形状重构
b2 = np.array([[1,1],
              [0,1]]) # 矩阵的写法，中间要 逗号间隔

c1 = np.dot(a4,b2)# 2种乘法
c2 = a4.dot(b2)
print("c1:%s\nc2:%s"%(c1,c2))
# print("a4:%s\na4+b2:%s\na4-b2:%s\na4*b2:%s\nb4**2:%s"%(a4,a4+b2,a4-b2,a4*b2, a4**2))
print('***'*15)

# (3)（4） 生成随机数组  二维 多维  求最大 最小 平均  axis用法
a5 = np.random.random((2,4))
print(a5)
print("最大值：%s\n最小值：%s\n和：%s\n平均值：%s"%(np.max(a5),np.min(a5),np.sum(a5),np.average(a5)))
print("每行最大值：%s\n每列最小值：%s\n每行数值总和：%s\n每列平均值：%s"%(np.max(a5,axis=0),np.min(a5,axis=1),np.sum(a5,axis=1),np.average(a5,axis=0)))
print('***'*15)

# (5) argmax/argmin:最大/小元素对应的索引
A = np.arange(2,14).reshape(3,4)
print(A)
print("A中最大元素的索引：%s\nA中最小元素的索引：%s"%(np.argmax(A),np.argmin(A)))
print('***'*15)

# （6）元素累加 元素累差
print(np.cumsum(A)) # [ 2  5  9 14 20 27 35 44 54 65 77 90]
print(np.diff(A)) # 每一行中后一项与前一项之差。故一个3行4列矩阵通过函数计算得到的矩阵便是3行3列的矩阵
print('***'*15)

# (7) 2种转置方法
print(np.transpose(A))
print(A.T)
print('***'*15)

# (8)将矩阵的元素替换为指定范围大小的值
print(np.clip(A,5,9))