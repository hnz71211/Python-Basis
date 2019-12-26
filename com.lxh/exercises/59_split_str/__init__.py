#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 提取 url 字符串 ‘https://blog.csdn.net/xufive’ 中的协议名
s = 'https://blog.csdn.net/xufive'
print(s.split("//")[0][:-1])