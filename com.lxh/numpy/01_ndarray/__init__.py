#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# 一维数组
# 创建数组
# 我们在写数组的时候是横着写的, 而其实数组是列向量
np.array([1, 2, 3])
np.ones(3)
np.zeros(3)
np.random.random(3)

# 数组运算
data = np.array([1, 2])
ones = np.ones(2)
data + ones
data * 1.6

# 数组索引
data = np.array([1, 2, 3])
data[0]
data[0: 2]
data[1:]

# 数组聚合
data = np.array([1, 2, 3])
data.max()
data.min()
data.sum()



# 二维数组，也就是矩阵
# 创建矩阵
np.array([[1, 2], [3, 4]])
np.ones((3, 2)) # 3行2列
np.zeros((3, 2))
np.random.random((3, 2))

# 运算
data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.ones(2)
data + ones_row

# 矩阵点积
matrix1 = np.array([1, 2, 3])
matrix2 = np.array([[1, 10], [100, 1000], [10000, 100000]])
print(matrix1.dot(matrix2))

# 矩阵索引
data = np.array([[1, 2], [3, 4], [5, 6]])
data[0, 1] # 1行2列 (2)
data[1: 3] # 2～3行 (array([[3, 4], [5, 6]]))
data[0: 2, 0] # 0~1行，1列 (array([1, 3]))

# 矩阵聚合
data = np.array([[1, 2], [3, 4], [5, 6]])
data.max()
data.min()
data.sum()
# 按行/列聚合
data.max(axis=0) # array([5, 6])
data.max(axis=1) # array([2, 4, 6])

# 矩阵转置
data.T

# 矩阵重塑
data = np.array([1, 2, 3, 4, 5, 6])
data.reshape(2, 3)
data.reshape(3, 2)



# 高维数组
# 创建
np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])



















