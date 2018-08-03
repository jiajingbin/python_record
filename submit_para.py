###总结实例：可变参数 关键字参数 命名关键字参数
##可变参数：允许传入0个或人一个参数，这些参数调用时自动组装成一个tuple
#1.传参个数不确定
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#调用时要组装一个list或者tuple
print('list:calc([1, 2, 3])=', calc([1, 2, 3]))
print('tuple:calc((1, 2, 3))=', calc((1, 2, 3)))
#--result:       list:calc([1, 2, 3])= 14
#--result:       tuple:calc((1, 2, 3))= 14

#2.利用可变参数:参数前面加*，numbers收到一个tuple
def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print('calc_1(1, 2, 3)=', calc_1(1, 2, 3))
#--result:       calc_1(1, 2, 3)= 14

#如果有一个list或者tuple，如何调用可变参数:*nums表示把nums这个list
#的所有元素作为可变参数传进去
nums = [1,3,5]
print('calc_1(*nums)=', calc_1(*nums))
#--result:       calc_1(*nums)= 35


##关键字参数：允许传入0个或任意个含参数名的参数
#这些关键字参数在函数内部自动组装成一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('jiajingbin', 29)
#--result:       name: jiajingbin age: 29 other: {}
person('Bob', 35, city='Beijing')
#--result:       name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
#--result:       Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#先组成dict在转换为关键字参数传参
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
#--result:       Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#**extra表示把extra这个dict的所有key-value用关键字参数
#传入到函数的**kw参数，kw将获得一个dict

##命名关键字参数：要限制关键字传参的名字
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
#如下只接收city和job作为关键字参数，且可以有缺省值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')
person('Jack', 24, city='shenzhen', job='Engineer')
#--result:       Jack 24 Beijing Engineer
#--result:       Jack 24 shenzhen Engineer

###参数混合
##参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
#--result:       a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
#--result:       a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
#--result:       a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
##最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#--result:       a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (2, 4, 6)
kw = {'d':99, 'x':'#'}
f2(*args,**kw)
#--result:       a = 2 b = 4 c = 6 d = 99 kw = {'x': '#'}

'''
小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。
'''
