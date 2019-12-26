#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断对象类型，使用type()函数
type(123)   # <class 'int'>
type('str') # <class 'str'>
type(None)  # <type(None) 'NoneType'>

# 如果一个变量指向函数或者类，也可以用type()判断：
type(abs)   # <class 'builtin_function_or_method'>
class Animal(object):
    def __init__(self):
        pass
a = Animal()
type(a)     # <class '__main__.Animal'>

# type()函数返回的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
type(123)==type(456)    # True
type(123)==int          # True
type('abc')==type('123')    # True
type('abc')==str        # True
type('abc')==type(123)  # False

# 要判断一个对象是否是函数, 可以使用types模块中定义的常量
import types
def fn():
    pass
type(fn)==types.FunctionType    # True
type(abs)==types.BuiltinFunctionType    # True
type(lambda x: x)==types.LambdaType     # True
type((x for x in range(10)))==types.GeneratorType   # True



# 优先使用isinstance()判断类型
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
# 能用type()判断的基本类型也可以用isinstance()判断：
isinstance('a', str)    # True
isinstance(123, int)    # True
isinstance(b'a', bytes) # True
# 还可以判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))    # True
isinstance((1, 2, 3), (list, tuple))    # True





# dir()函数，要获得一个对象的所有属性和方法，它返回一个包含字符串的list
# 比如，获得一个str对象的所有属性和方法
dir('ABC')      # ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

# len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价
len('ABC')  # 3
'ABC'.__len__() # 3
# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
len(dog)    # 100





# getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
#紧接着，可以测试该对象的属性：
# 有属性'x'吗？
hasattr(obj, 'x')   # True
obj.x   # 9
# 有属性'y'吗？
hasattr(obj, 'y')   # False
# 设置一个属性'y'
setattr(obj, 'y', 19)
hasattr(obj, 'y')   # True
# 获取属性'y'
getattr(obj, 'y')   # 19
# 获取属性'y'
obj.y   # 19
# 获取属性'z', 试图获取不存在的属性，会抛出AttributeError的错误
getattr(obj, 'z')   # AttributeError: 'MyObject' object has no attribute 'z'
# 获取属性'z'，如果不存在，返回默认值404
getattr(obj, 'z', 404)  # 404

# 获得对象的方法
# 有属性'power'吗？
hasattr(obj, 'power')   # True
# 获取属性'power'
getattr(obj, 'power')   # <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn = getattr(obj, 'power')   # fn指向obj.power
fn  # <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# 调用fn()与调用obj.power()是一样的
fn()    # 81



# 只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
sum = obj.x + obj.y
# 就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')

# 一个正确的用法的例子如下：
"""
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
"""
























