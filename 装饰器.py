#一个完整的decorator的写法如下：
import functools
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
#或者针对带参数的decorator：
import functools
    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

#import functools是导入functools模块。模块的概念稍候讲解。
#现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可
