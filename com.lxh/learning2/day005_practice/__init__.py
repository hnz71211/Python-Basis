from math import sqrt

# 练习1：生成斐波那契数列的前20个数。
f = 1
l = 1
# n = int(input('输入n: '))
n = 20

for i in range(n):
    if i == 0 or i == 1:
        print('1', end=' ')
    else:
        print('%d' % (f + l), end=' ')
        f,l = l, f + l

print()

# 练习2： 找出10000以内的完美数
# 例如： 6（6=1+2+3）和28（28=1+2+4+7+14）就是完美数
for i in range(1, 10000):
    sum = 0
    for j in range(1, int(i / 2) + 1):
        if i % j == 0:
            sum += j
    if i == sum:
        print('%d' % i, end=' ')

print()

# 练习3：输出100以内所有的素数
for i in range(2, 100):
    end = int(sqrt(i))
    is_prime = True
    for x in range(2, end + 1):
        if i % x == 0:
            is_prime = False
            break
    if is_prime:
        print('%d' % i, end=' ')




