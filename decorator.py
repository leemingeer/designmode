#!/usr/bin/env python
#encoding=utf-8
#Python与设计模式--装饰器模式
#动态地给一个对象添加一些额外的职责
#优点：
#1、装饰器模式是继承方式的一个替代方案，可以轻量级的扩展被装饰对象的功能；
#2、Python的装饰器模式是实现AOP的一种方式，便于相同操作位于不同调用位置的统一管理。
#AOP即Aspect Oriented Programming，中文翻译为面向切面的编程，它的含义可以解释为：如果几个或更多个逻辑过程中（这类逻辑过程可能位于不同的对象，不同的接口当中），有重复的操作行为，就可以将这些行为提取出来（即形成切面），进行统一管理和维护。举例子说，系统中需要在各个地方打印日志，就可以将打印日志这一操作提取出来，作为切面进行统一维护。

#应用场景：
#1、需要扩展、增强或者减弱一个类的功能，如本例。
class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

class drinkDecorator():
    def getName(self):
        pass
    def getPrice(self):
        pass

class iceDecorator(drinkDecorator):
    def __init__(self,beverage):
        self.beverage=beverage
    def getName(self):
        return self.beverage.getName()+" +ice"
    def getPrice(self):
        return self.beverage.getPrice()+0.3
    
class sugarDecorator(drinkDecorator):
    def __init__(self,beverage):
        self.beverage=beverage
    def getName(self):
        return self.beverage.getName()+" +sugar"
    def getPrice(self):
        return self.beverage.getPrice()+0.5

if  __name__=="__main__":
    coke_cola=coke()
    print "Name:%s"%coke_cola.getName()
    print "Price:%s"%coke_cola.getPrice()
    ice_coke=iceDecorator(coke_cola)
    print "Name:%s" % ice_coke.getName()
    print "Price:%s" % ice_coke.getPrice()