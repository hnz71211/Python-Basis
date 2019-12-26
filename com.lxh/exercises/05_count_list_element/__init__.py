#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数
a = [True, False, 0, 1, 2]
# count()不区分True和1、False和0，但None、''不会被视为False
print(a.count(True), a.count(False), a.count(0), a.count(1), a.count(2))

