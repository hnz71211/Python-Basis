#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断 ‘https://blog.csdn.net’ 是否以 ‘http://’ 或 ‘https://’ 开头。若是，则返回 ‘http’ 或 ‘https’；否则，返回None。

def get_url_start(url):
    return url.split(":")[0] if url.startswith(('http://', 'https://')) else None

s = 'https://blog.csdn.net'
print(get_url_start(s))