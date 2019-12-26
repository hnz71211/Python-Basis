#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 03_tuple，元组，有序列表。tuple一旦初始化就不能修改
# 没有append(), insert()方法
classmates = ('Michael', 'Bob', 'Tracy')

# 空的tuple
t = ()

# 定义一个只有一个元素的tuple,若不加逗号，括号会产生歧义，所以只有1个元素的tuple必须加逗号
t = (1,)

# '可变的'03_tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
