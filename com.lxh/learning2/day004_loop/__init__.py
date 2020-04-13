from math import sqrt

"""
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。
"""

# 练习1：输入一个正整数判断是不是素数。
num = int(input('input a number: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d is prime' % num)
else:
    print('%d is not prime' % num)


# 练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
a = int(input('number a: '))
b = int(input('number b: '))
if a > b:
    a, b = b, a
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print('最大公约数:%d' % factor)
        print('最小公倍数:%d' % (a * b / factor))
        break


# 练习3：打印三角形图案。
row = 5
for i in range(row):
    for j in range(i + 1):
        print('*', end='') # print默认是换行的
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()