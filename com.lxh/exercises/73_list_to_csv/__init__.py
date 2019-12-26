#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将二维列表 [[0.468,0.975,0.446],[0.718,0.826,0.359]] 写成名为 csv_data 的 csv 格式的文件，并尝试用 excel 打开它
L = [[0.468, 0.975, 0.446], [0.718, 0.826, 0.359]]
with open(r'/users/hexli/downloads/csv_data.csv', 'w') as fp:
    for row in L:
        line_len = fp.write('%s\n' % (','.join([str(col) for col in row])))