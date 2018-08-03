#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
#在代码运行的时候，总是会调用子类的run()。

class Animal(object):
    def run(self):
        print('Animal is running')
class Dog(Animal):
    def run(self):
        print('dog is running')
class Cat(Animal):
    def run(self):
        print('cat is running')

#多态：由于Animal类型有run()方法，因此，传入的任意类型，
#只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数

def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

