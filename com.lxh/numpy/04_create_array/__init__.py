#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
# shape	数组形状
# dtype	数据类型，可选
# order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
# numpy.empty(shape, dtype = float, order = 'C')
x = np.empty([3,2], dtype = int)

# 创建指定大小的数组，数组元素以 0 来填充：
# numpy.zeros(shape, dtype = float, order = 'C')
# 默认为浮点数
x = np.zeros(5)
# 设置类型为整数
y = np.zeros((5,), dtype=np.int)
# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])

# 创建指定形状的数组，数组元素以 1 来填充：
# numpy.ones(shape, dtype = None, order = 'C')
# 默认为浮点数
x = np.ones(5)
# 自定义类型
x = np.ones([2, 2], dtype=int)