#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17
dict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
dict.update({'David', 19})
dict.update({'Cecil', 17})
print(dict)
