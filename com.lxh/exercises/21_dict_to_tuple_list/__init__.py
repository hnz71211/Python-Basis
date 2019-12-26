#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组
dict = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
L = list(dict.items())
print(L)