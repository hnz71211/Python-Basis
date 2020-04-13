import time
import json


"""
操作模式	具体含义
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""


def f1():
    f = None
    try:
        f = open('abc.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()


def f2():
    try:
        # 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
        with open('abc.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')


def f3():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)



def f4():
    filenames = ('a.txt', 'b.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 100):
            if number < 50:
                fs_list[0].write(str(number) + '\n')
            else:
                fs_list[1].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误！')
    finally:
        for fs in fs_list:
            fs.close()



# 读写二进制文件
def f5():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data)) # <class 'bytes'>
        with open('guido_bak.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')



# 读写JSON文件
"""
JSON	Python
object	dict
array	list
string	str
number (int / real)	int / float
true / false	True / False
null	None
"""
"""
json模块主要有四个比较重要的函数，分别是：
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""
def f6():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)