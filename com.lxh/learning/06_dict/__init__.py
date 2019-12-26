#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置了字典dict，其他语言也称为map，使用key-value存储，具有极快的查找速度

d = {'Michael':95, 'Bob': 75, 'Tracy': 85}
d['Michael'] #95

# 通过key放入dict
d['Adam'] = 67

# 如果key不存在，dict会报错
#d['Thomas']

# 避免key不存在，有两种办法
# in
'Thomas' in d #False
# get(),如果不存在，返回None，或者指定的value
d.get('Thomas') #None
d.get('Thomas', -1) #-1

# 对应的value也会从dict中删除
d.pop('Bob')
