#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对
dict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
for k, v in dict.items():
    print('key: %s, value: %d' % (k, v))