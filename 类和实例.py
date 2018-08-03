#Student类
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' %(self.name, self.score))

s = Student('jiajingbin', 77)
s.print_score()
#可直接修改值
s.name = 'add'
print(s.name)
print(s.score)


#数据封装
def print_score(std):
    
    print('%s::%s' %(std.name, std.score))
my_score = Student('jia', 100)
my_score.print_score()
print_score(my_score)

#访问限制
#上面的例子中，外部代码可以自由修改实例中的name和score
#如果要让内部属性不被外部访问，可以在属性前加__
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
#>>> bart = Student('Bart Simpson', 98)
#>>> bart.__name
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#AttributeError: 'Student' object has no attribute '__name'

#通过添加get_name和get_score方法可以获取name和score
#通过set_score方法可以修改score
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
#以一个下划线开头的实例变量名外部是可以访问的
#但是 虽然我可以被访问，但是，请把我视为私有变量，不要随意访问

        
