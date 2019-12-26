#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 如果不立刻求和，而是在后面的代码中，根据需要再计算
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 可以不返回求和的结果，而是返回求和的函数
f = lazy_sum(1, 3, 5, 7, 9)
f   # <function lazy_sum.<locals>.sum at 0x101c6ed90>
f() # 25


# 在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，相关参数和变量都保存在返回的函数中
# 这种称为“闭包（Closure）”

# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1==f2  # False


# 函数f()未立刻执行，等到3个函数都返回时，i变成了3，所以结果为9 9 9
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count() # [<function count.<locals>.f at 0x101a78ef0>, <function count.<locals>.f at 0x101a78dd0>, <function count.<locals>.f at 0x101a8c560>]
f1()    # 9
f2()    # 9
f3()    # 9

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量, 再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
f1()    # 1
f2()    # 4
f3()    # 9