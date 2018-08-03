解析Python中的yield关键字




前言
 
python中有一个非常有用的语法叫做生成器，所利用到的关键字就是yield。有效利用生成器这个工具可以有效地节约系统资源，避免不必要的内存占用。
 
一段代码
def fun():
    for i in range(20):
        x=yield i
        print('good',x)

if __name__ == '__main__':
    a=fun()
    a.__next__()
    x=a.send(5)
    print(x) 
这段代码很短，但是诠释了yield关键字的核心用法，即逐个生成。在这里获取了两个生成器产生的值，即0和1。分别由next函数和send()函数获得，这两个函数的区别我们后面会详细阐述。
 关于__next__函数，这里先说明一下，我们可以利用__next__()这个函数持续获取符合fun函数规则的数，直到19结束。这段代码如下所示：
def fun():
    for i in range(20):
        x=yield i

if __name__ == '__main__':
    for x in fun():
        print(x) 
这段代码的效果和下面这段代码是完全相同的
if __name__ == '__main__':
    for i in range(20):
        x=yield i 
for..in调用生成器算是生成器的基础用法，不过只会用for..in意义是不大的。生成器中最重要的函数是sent和__next__这两个函数，下面就针对这两个函数进行详细的阐述。
 
sent函数
 
这里特别强调了sent函数，因为sent函数没有那么直观。__next__函数很好理解，就是从上一个终止点开始，到下一个yield结束，返回值就是yield表达式的值。
 例如在初始的那段代码里：
def fun():
    for i in range(20):
        x=yield i
        print('good',x) 
第一次调用__next__函数的时候，我们从fun的起点开始，然后在yield处结束，需要注意的是，赋值语句不会调用，此处yield i和含义和return差不多。
 但是第二次调用__next__函数的时候，就会直接从上一个yield的结束处开始，也就是先执行赋值语句，然后输出字符串，进入下一个循环，直到下一个yield或者生成器结束
 再次看初始的那段代码，可以发现第二次调用的时候没有选择使用__next__函数，而是使用了一个sent()函数。这里就需要注意，sent()函数的用法和__next__函数不太一样。sent()函数只能从yield之后开始，到下一个yield结束。这也就意味着第一次调用必须使用__next__函数。
 sent()函数最重要的作用在于它可以给yield对应的赋值语句赋值，比如上面那一段代码中的
     x=yield i 
如果调用__next()__函数，那么x=None。但是如果调用sent(5)，那么x=5。除了上述将的两个特征以外，sent和next并没有什么区别，sent函数也会返回yield表达式对应的值
 
next函数调用次可能有限
 
需要特别注意的是，尽管是生成器。但是next函数的调用次数可能是有限的。比如下面这段代码
def fun():
    for i in range(20):
        x=yield i
        print('good',x)

if __name__ == '__main__':
    a=fun()
    for i in range(30):
        x=a.__next__()
        print(x) 
生成器里的函数只循环了20次，但是next函数却调用了30次，这时候就会触发StopIteration异常。
