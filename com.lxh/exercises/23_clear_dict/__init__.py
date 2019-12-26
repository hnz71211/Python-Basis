#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典
dict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
dict.pop('Beth')
print(dict)
dict.clear()
print(dict)