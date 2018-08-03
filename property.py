#原始函数
class Student(object):
    def get_score(self):
        return self.__score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be int')
        if value <0 or value >100:
            raise ValueError('score must be 0-100')
        self.__score = value

s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(999)

#Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student_pro(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be int')
        if value <0 or value >100:
            raise ValueError('score should be 0-100')
        self.__score = value

s_pro = Student_pro()
s_pro.score = 99
print(s_pro.score)
