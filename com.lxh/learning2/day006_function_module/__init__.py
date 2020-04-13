from module1 import foo
import module2 as m2
import module3

# 函数的参数


# 在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持函数的重载
def add(a=0, b=0, c=0):
    return a + b + c

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))



# 对0个或多个参数进行加法运算，而具体有多少个参数是由调用者来决定，
# 因此在不确定参数个数的时候，我们可以使用可变参数
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))



# 使用函数的时候通过import关键字导入指定的模块
# 就可以区分到底要使用的是哪个模块中的foo函数
foo()
m2.foo()


# -------------------------------------------------------------------
# 练习1：实现计算求最大公约数和最小公倍数的函数。
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x, y):
    return x * y // gcd(x, y)

# 练习2：实现判断一个数是不是回文数的函数。
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

# 练习3：实现判断一个数是不是素数的函数。
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


# 变量作用域
def outer():
    # outer函数中我们定义了变量b，这是一个定义在函数中的局部变量（local variable），属于局部作用域，在outer函数的外部并不能访问到它
    b = 'hello'

    # Python中可以在函数内部再定义函数
    # inner函数，变量b属于嵌套作用域，在inner函数中我们是可以访问到它的。inner函数中的变量c属于局部作用域，在inner函数之外是无法访问的
    def inner():
        c = True
        print(a)
        print(b)
        print(c)

    inner()
    # print(c)  # NameError: name 'c' is not defined

if __name__ == '__main__':
    # if分支中定义了一个变量a，这是一个全局变量（global variable），属于全局作用域
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    outer()



# global关键字
# 我们希望通过函数调用修改全局变量a的值，但实际上下面的代码是做不到的
# 因为当我们在函数modify中写a = 200的时候，是重新定义了一个名字为a的局部变量，它跟全局作用域的a并不是同一个变量，因为局部作用域中有了自己的变量a
def modify():
    a = 200
    print(a)  # 200
if __name__ == '__main__':
    a = 100
    modify()
    print(a)  # 100
# 使用global关键字来指示modify函数中的变量a来自于全局作用域，如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域
def modify():
    global a
    a = 200
    print(a)  # 200
if __name__ == '__main__':
    a = 100
    modify()
    print(a)  # 200