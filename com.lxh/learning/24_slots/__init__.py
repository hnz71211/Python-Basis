#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')
s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
s.score = 99 # 绑定属性'score', 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
"""
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用