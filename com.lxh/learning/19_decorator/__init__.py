#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）, 本质上，decorator就是一个返回函数的高阶函数

def log(func):
    # decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
    # 所以，用@functools.wraps(func)，把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 要借助Python的@语法，把decorator置于函数的定义处：
# 把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
@log
def now():
    print('2015-3-25')
now()
# call now():
# 2015-3-25


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
# now = log('execute')(now)
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()
# execute now():
# 2015-3-25