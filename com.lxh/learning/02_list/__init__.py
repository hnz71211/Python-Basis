#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是一种有序集合
classmates = ['Micheal', 'Bob', 'Tracy']

len(classmates)

classmates[0]

# 如果要去倒数第*个元素，可以用负数做索引
classmates[-1]

classmates.append('Adam')

# 插入到索引为1的位置
classmates.insert(1, 'Jack')

# 删除list末尾的元素
classmates.pop()

classmates[1] = 'Sarah'

# list里面的元素可以不同
L = ['Apple', 123, True, ['asp', 'php']]
L[3][1] #'php'

