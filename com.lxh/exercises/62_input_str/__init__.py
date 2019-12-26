#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串
def printMobileNumber():
    num = input('输入手机号：')
    print('Mobile: %s %s %s' % (num[0:3], num[3:7], num[7:]))

printMobileNumber()