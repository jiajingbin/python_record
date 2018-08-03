###递归：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#计算n阶乘
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#这种方法递归次数调用过多会导致栈溢出
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
#尾递归
def fact_1(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num*product)
'''
可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，
num - 1和num * product在函数调用前就会被计算，不影响函数调用。
fact(5)对应的fact_iter(5, 1)的调用如下：
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
'''
fact_1(5)

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')






