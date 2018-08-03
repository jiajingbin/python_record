def html_tags(tag_name):
    def wrapper_(func):
        print('func:', func())
        def wrapper(*args, **kwargs):
            print('*args:',args)
            print('**kwargs:',kwargs)
            content = func(*args, **kwargs)
            print('content:', content)
            return "<{tag}>{content}</{tag}>".format(tag=tag_name, content=content)
        return wrapper
    return wrapper_
def hello(name='jiajingbin'):
    return 'hello {}'.format(name)

hello = html_tags('b')(hello)
print(hello())
#print(hello('world'))
