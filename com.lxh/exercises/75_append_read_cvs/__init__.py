#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 向 csv_data.csv 文件追加二维列表 [[1.468,1.975,1.446],[1.718,1.826,1.359]]，然后读出所有数据
L = [[1.468, 1.975, 1.446], [1.718, 1.826, 1.359]]
with open(r'/users/hexli/downloads/csv_data.csv', 'a') as fp:
    for row in L:
        line_len = fp.write('%s\n' % (','.join([str(col) for col in row])))

data = list()
with open(r'/users/hexli/downloads/csv_data.csv', 'r') as fp:
    for line in fp.readlines():
        data.append([float(item) for item in line.strip().split(',')])
print(data)