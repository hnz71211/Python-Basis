#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (object)，表示该类是从哪个类继承下来的
class Student(object):
    # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    def __init__(self, name, score):
        # self.name = name
        # self.score = score

        # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score

    def print_score(self):
        # print('%s: %s' % (self.name, self.score))
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
bart = Student('Bart Simpson', 59)
bart.print_score()