#coding: utf-8
#encoding=utf-8
#ref: https://www.jianshu.com/p/08d7956601de
#     https://www.cnblogs.com/Xjng/p/4029563.html
#basic background
class Person(object):

    def __new__(cls, name, age):
        print '__new__ called.'
        return super(Person, cls).__new__(cls, name, age)

    def __init__(self, name, age):
        print '__init__ called.'
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)
#if __name__ == '__main__':
#    name = Person('xxx', 24)
#    print name
#output:
#__new__ called.
#__init__ called.
#<Person: xxx(24)>
#1.p = Person(name, age)
#2.首先执行使用name和age参数来执行Person类的new方法，这个new方法会 返回Person类的一个实例（通常情况下是使用 super(Persion, cls).new(cls, … …) 这样的方式），
#3.然后利用这个实例来调用类的init方法，上一步里面new产生的实例也就是 init里面的的 self

#.init 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
#    new 通常用于控制生成一个新实例的过程。它是类级别的方法。
#    new至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
#    new必须要有返回值，返回实例化出来的实例，
class PositiveInteger(int):
    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))

i = PositiveInteger(-3)
print i
#这是因为对于int这种 不可变的对象，我们只有重载它的new方法才能起到自定义的作用

class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

i = PositiveInteger(-3)
print i

__author__ = 'leemingeer@qq.com'

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_the_instance'):
            cls._the_instance=object.__new__(cls,*args, **kwargs)
        return cls._the_instance

class A(Singleton):
    print 'init before'
    def __init__(self):
        print 'i am __init__'
    def f(self):
        print 'i am f'

a=A()
b=A()
a.f()
print id(a)
print id(b)
print 'done'