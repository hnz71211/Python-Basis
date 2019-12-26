#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 写一个函数，以0.1秒的间隔不换行打印30次由函数参数传入的字符，实现类似打字机的效果
import time
def printParams(ch, n = 30, delay = 0.1):
    for i in range(n):
        print(ch, end = '', flush = True)
        time.sleep(delay)

printParams("*")