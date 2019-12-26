#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一边循环一边计算的机制，称为生成器：generator

# L是一个list，而g是一个generator
L = [x * x for x in range(10)]      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))      # <generator object <genexpr> at 0x1022ef630>
# next()函数获得generator的下一个返回值
next(g)     # 0
next(g)     # 1


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
f       # <generator object fib at 0x104feaaa0>

# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
# odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
next(o)
# step 1
# 1
next(o)
# step 2
# 3
next(o)
# step 3
# 5
next(o)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration