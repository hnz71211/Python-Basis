#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 默认参数
# 当调用power(5)时， 相当于调用power(5, 2)
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 多次调用add_end()，结果是不一样的
def add_end(L=[]):
    L.append('END')
    return L
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L




# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2)
calc()
# *nums表示把nums这个list的所有元素作为可变参数传进去。
nums = [1, 2, 3]
calc(*nums)






# 关键字参数，允许传入0个或任意个含参数名的参数，这些参数在函数内自动组装成一个dict
# 关键字参数kw
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)   # name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing')   # name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')  # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) #vname: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}






# 关键字参数，函数的调用者可以传入任意不受限制的关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
# 调用者传入不受限制的关键字参数
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 命名关键字参数，限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)




# 参数组合，用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}