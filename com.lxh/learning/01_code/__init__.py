print('包含中文字符的str')

# ord()函数获取字符的整数表示
ord('A') #65
ord('中') #20013

# chr()函数把编码转换成对应的字符
chr(66) #'B'
chr(25991) #'文'

# 对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
'ABC'.encode('ascii') #b'ABC'
'中文'.encode('utf-8') #b'\xe4\xb8\xad\xe6\x96\x87'
#'中文'.encode('ascii') #Traceback (most recent call last):

# decode() 把bytes变为str
b'ABC'.decode('ascii') #'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') #'中文'

# len() 计算str的字符数
len(b'ABC') #3
len(b'\xe4\xb8\xad\xe6\x96\x87') #6
len('中文'.encode('utf-8')) #6

# str和bytes的互相转换，为了避免乱码问题，应当始终使用utf-8对str和bytes进行转换。
# 当Python解释器读取源代码时，为了让它按utf-8读取编码，通常在文件开头写上这两行
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello, %s, %d, %f' % ('world', 999, 12.34))