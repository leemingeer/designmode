#!/usr/bin/env python
#encoding=utf-8
#ref:https://yq.aliyun.com/articles/70416?spm=a2c4e.11154837.922301.7.6feb20adu2NwQw
#Python与设计模式--建造者模式


#zhushi
class Burger():
    name=""
    price=0.0
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0
#------------------------------------
#lingshi
class Snack():
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0

#---------------------------------------
#yinliao
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

#--------------------------------------
#建造者模式的定义如下：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
class order():
    burger=""
    snack=""
    beverage=""
    def __init__(self,orderBuilder):
        self.burger=orderBuilder.bBurger
        self.snack=orderBuilder.bSnack
        self.beverage=orderBuilder.bBeverage
    def show(self):
        print "Burger:%s"%self.burger.getName()
        print "Snack:%s"%self.snack.getName()
        print "Beverage:%s"%self.beverage.getName()
    
class orderBuilder():
    bBurger=""
    bSnack=""
    bBeverage=""
    def addBurger(self,xBurger):
        self.bBurger=xBurger
    def addSnack(self,xSnack):
        self.bSnack=xSnack
    def addBeverage(self,xBeverage):
        self.bBeverage=xBeverage
    def build(self):
        return order(self)
    
class orderDirector():
    order_builder=""
    def __init__(self,order_builder):
        self.order_builder=order_builder
    def createOrder(self,burger,snack,beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()   


if  __name__=="__main__":
    order_builder=orderBuilder()
    #m1
    #order_builder.addBurger(spicyChickenBurger())
    #order_builder.addSnack(chips())
    #order_builder.addBeverage(milk())
    #order_1=order_builder.build()
    #order_1.show()
    #m2
    orderdirector = orderDirector(order_builder)
    od = orderdirector.createOrder(spicyChickenBurger(), chips(), milk())
    od.show()