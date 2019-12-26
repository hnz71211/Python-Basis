#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

# isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
isinstance([], Iterable)    # True
isinstance({}, Iterable)    # True
isinstance('abc', Iterable) # True
isinstance((x for x in range(10)), Iterable)    # True
isinstance(100, Iterable)   # False

# 可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
isinstance((x for x in range(10)), Iterator)    #True
isinstance([], Iterator)    #False
isinstance({}, Iterator)    #False
isinstance('abc', Iterator)     #False

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
isinstance(iter([]), Iterator)  # True
isinstance(iter('abc'), Iterator)   # True

# Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的