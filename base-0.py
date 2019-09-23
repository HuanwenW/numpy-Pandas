# -*- coding:utf8 -*-

import numpy as np

# ------代码学习知识点及代码示例------ #
""""
numpy常用几种属性用法及数组创建的一些高级用法：

(1)  xxx.ndim : 维度
(2)  xxx.shape:行数 和 列数
(3)  xxx.size :元素个数  

(4)  np.array : 创建数组
(5)  np.dtype : 指定数据类型

(6)  np.zeros():创建数据全为0
(7)  np.ones() :创建数据全为1  
(8)  empty : 创建数据接近于0（科学计数法表示才能看出，此例子中输出为 0.）
(9)  arrange: 按指定范围创建数据
(10) linspace :创建字段

"""

# (1)(2)(3)定义一个数组, 查看常用属性
array =np.array([[1,2,3],
                 [4,5,6]])
print(array) #
print(array.ndim) # 2
print(array.shape) # (2,3)
print(array.size) # 6

print('***'*15)


# （4）单纯的创建数组  #
a = np.array([5,20,1314])
print(a) # [   5   20 1314]

# （5）创建 指定数据类型 的数组  #
b_1 = np.array([5,20,1314],dtype=np.int32)
b_2 = np.array([5,20,1314],dtype=np.float)
b_3 = np.array([5,20,1314],dtype=np.float32)
print(b_1.dtype) # int32
print(b_2)       # [   5.   20. 1314.] 由整型变为浮点型，数值后多了一个 .
print(b_2.dtype) # float64
print(b_3.dtype) # float32
print('***'*10)

# （6）（7）（8）创建 特定的数据  #

c_1 = np.zeros((3,4))
c_2 = np.zeros((3,4),dtype=np.float32)
print(c_2)      # 3行4列 全为 0. 的数

print('\n')

c_3 = np.ones((2,5),dtype=np.int)
print(c_3)      # 2行5列 全为 1 的数

print('\n')

c_4 = np.empty((2,3))
print(c_4)      # 2行3列 接近 0 的数（输出结果全为 0 ，但是用科学计数法表示的话是很接近 0 的数）

print('\n')

# （9）（10）创建 指定范围的数据  #

d_1 = np.arange(7,20,2) # 7 到 19 之间的数据，步长 = 2
d_2 = np.arange(12).reshape((3,4)) # 生成 3行4列的矩阵，且取值范围 0 到 11 之间
print(d_1)
print(d_2)

print('\n')

e_1 = np.linspace(1,10,20) # 第一个数 = 1， 最后一个数 = 10 ，一共分割成20个数据，生成险段

e_2 = np.linspace(1,10,20).reshape(4,5) # 生成 3行4列的矩阵， 且第一个数 = 1， 最后一个数 = 10 ，一共分割成20个数据，生成险段
print(e_1)
print(e_2)
