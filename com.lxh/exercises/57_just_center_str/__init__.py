#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果
L = ['Hello, 我是David', 'OK, 好', '很高兴认识你']
L_len = [len(item) for item in L]   # 各个字符串长度
L_len_gbk = [len(item.encode('gbk')) for item in L] # 各字符串中gbk编码的字节长度
c_num = [a - b for a, b in zip(L_len_gbk, L_len)]   # 各字符串中包含的中文符合个数
len_max = max(L_len_gbk)    # 最大字符串占位长度

for s, c in zip(L, c_num):
    print('"%s"' % s.ljust(len_max - c))

for s, c in zip(L, c_num):
    print('"%s"' % s.rjust(len_max - c))

for s, c in zip(L, c_num):
    print('"%s"' % s.center(len_max - c))