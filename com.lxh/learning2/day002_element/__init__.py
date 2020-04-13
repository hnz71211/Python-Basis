# 使用变量保存数据并进行算术运算
a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 使用type()检查变量的类型
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# Python中内置的函数对变量类型进行转换
# int()：将一个数值或字符串转换成整数，可以指定进制。
# float()：将一个字符串转换成浮点数。
# str()：将指定的对象转换成字符串形式，可以指定编码。
# chr()：将整数转换成该编码对应的字符串（一个字符）。
# ord()：将字符串（一个字符）转换成对应的编码（整数）。


"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串,
    print函数中输出的字符串使用了占位符语法，其中%d是整数的占位符，%f是小数的占位符，%%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%)
"""
a = int(input('a = '))
b = int(input('b = '))
#
print('%d + %d = %d' % (a, b, a + b))


"""
运算符	        描述
[] [:]	        下标，切片
**	            指数
~ + -	        按位取反, 正负号
* / % //	    乘，除，模，整除
+ -	            加，减
>> <<	        右移，左移
&	            按位与
^ |	            按位异或，按位或
<= < > >=	    小于等于，小于，大于，大于等于
== !=	        等于，不等于
is is not	    身份运算符
in not in	    成员运算符
not or and	    逻辑运算符
"""


# 比较、逻辑和算身份运算符的使用
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False

# --------------------------------------------------------------------------

# 练习1：华氏温度转换为摄氏温度。C=(F−32)÷1.8。
f = float(input('F: '))
c = (f - 32) / 1.8
print('%.1fF = %.1fC: ' % (f, c))

# 练习2：输入圆的半径计算计算周长和面积。
import math
r = float(input('r= '))
l = 2 * r * math.pi
s = r ** 2 * math.pi
print('l = %.2f' % l)
print('s = %.2f' % s)

# 练习3：输入年份判断是不是闰年。
year = int(input('Year: '))
is_leap = (year % 4 ==0 and year % 100 != 0) \
          or year % 400 == 0
print(is_leap)