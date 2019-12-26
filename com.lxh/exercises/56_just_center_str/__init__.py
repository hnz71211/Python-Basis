#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果
L = ['ok', 'hello', 'thank you']
len_max = max([len(item) for item in L])    # 最大长度
for item in L:
    print('"%s"' % item.ljust(len_max))

for item in L:
    print('"%s"' % item.rjust(len_max))

for item in L:
    print('"%s"' % item.center(len_max))