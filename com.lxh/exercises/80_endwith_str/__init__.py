#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断 ‘https://blog.csdn.net’ 是否以 ‘.com’ 或 ‘.net’ 结束。若是，则返回 ‘com’ 或 ‘net’；否则，返回None
def get_url_end(url):
    return url.split('.')[-1] if url.endswith(('.com', '.net')) else None

print(get_url_end('https://blog.csdn.net'))