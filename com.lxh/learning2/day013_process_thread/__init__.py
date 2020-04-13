from multiprocessing import Process
from threading import Thread, Lock
from os import getpid
from random import randint
from time import time, sleep


# Python中的多进程
"""
通过Process类创建了进程对象，
通过target参数我们传入一个函数来表示进程启动后要执行的代码，args是一个元组，它代表了传递给函数的参数。
Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
"""

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def f1():
    start = time()
    p1 = Process(target=download_task, args=('a.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('b.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('%.2f second' % (end - start))


"""
最后的结果是Ping和Pong各输出了10个，Why？
当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，
每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量
"""
counter = 0
def sub_task(string):
    global counter
    while counter < 10:
        print(string, end=' ', flush=True)
        counter += 1
        sleep(0.01)
def f2():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()



# Python中的多线程,比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性
"""
使用threading模块，模拟文件下载
"""
def f3():
    start = time()
    t1 = Thread(target=download_task, args=('a.pdf', ))
    t1.start()
    t2 = Thread(target=download_task, args=('b.avi', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('%.2f second' % (end - start))


"""
通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
"""
class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))

def f4():
    t1 = DownloadTask('a.pdf')
    t1.start()
    t2 = DownloadTask('b.avi')
    t2.start()
    t1.join()
    t2.join()


"""
线程通信：设置全局变量
模拟100个线程向同一个银行账户转账（转入1元钱）的场景，
银行账户是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果。
"""
class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01s的时间
            sleep(0.001)
            # 修改账户余额
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()
    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def f5():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存款
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('total: %d yuan' % account.balance)



"""
在Python语言中，单线程+异步I/O的编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。
协程最大的优势就是极高的执行效率，因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销。
协程的第二个优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不用加锁，只需要判断状态就好了，
所以执行效率比多线程高很多。如果想要充分利用CPU的多核特性，最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
"""


if __name__ == '__main__':
    f5()