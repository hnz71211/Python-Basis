#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从 csv_data.csv 文件中读出二维列表
data = list()
with open(r'/users/hexli/downloads/csv_data.csv', 'r') as fp:
    for line in fp.readlines():
        data.append([float(item) for item in line.strip().split(',')])
print(data)