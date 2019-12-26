#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串

def printDatetime():
    df = input('输入年月日时分秒，空格分割：')
    Y, M, D, h, m, s = df.split()
    Y, M, D, h, m, s = int(Y), int(M), int(M), int(h), int(m), int(s)
    print('%4d-%2d-%2d %2d:%2d:%2d' % (Y, M, D, h, m, s))

printDatetime()