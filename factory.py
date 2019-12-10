#!/usr/bin/env python

#encoding=utf-8
# ref: https://blog.csdn.net/u011654843/article/details/99692401
# ref: https://www.jianshu.com/p/0cbd86e165e9
## 无工厂
class IPhone(object):
    #苹果
    def __repr__(self):
        return "IPhone"
class Huawei(object):
    # 华为
    def __repr__(self):
        return "Huawei"
#encoding=utf-8
class IMAC(object):
    #苹果
    def __repr__(self):
        return "IMAC"
class HuaweiMAC(object):
    # 华为
    def __repr__(self):
        return "HuaweiMAC"

#--------------------------------------------------
 ## 简单工厂 if else return different instance
from noFactory import IPhone, Huawei
 
class SimplePhoneFactory(object):
    #构造一个“简单工厂”把所有实例化的过程封装在里面。需要什么直接调工厂里的方法
    @staticmethod
    def get_phone(name):
        if name == 'iphone':
            return IPhone()
        elif name == 'huawei':
            return Huawei()
if __name__ == '__main__':
    print SimplePhoneFactory.get_phone('iphone')
    print SimplePhoneFactory.get_phone('huawei')


#-----------------------------------------------------------
# coding=utf-8
import abc
 
# 工厂方法
#在简单工厂的基础上抽象成不同的工厂，每个工厂对应生成自己的产品，这就是工厂方法
from noFactory import IPhone, Huawei
 
 
class AbstractFactory(object):
    # 抽象的工厂类
    __metaclass__ = abc.ABCMeta
 
    # python不同于java没有abstract抽象类关键字通过加载abc实现抽象方法
    @abc.abstractmethod
    def get_phone(self):
        pass
 
 
# 苹果工厂
class IPhoneFactory(AbstractFactory):
    def get_phone(self):
        return IPhone()
 
 
# 华为工厂
class HuaweiFactory(AbstractFactory):
    def get_phone(self):
        return Huawei()
if __name__ == '__main__':
    iphone = IPhoneFactory().get_phone()
    huawei = HuaweiFactory().get_phone()
    print iphone
    print huawei

#----------------------------------------------------
#抽象工厂方法
#当产品增多业务复杂时，例如工厂不仅生产手机还要生产电脑时面对这种业务场景，就需要使用抽象工厂方法
# coding=utf-8
import abc
from noFactory import IPhone, Huawei, IMAC, HuaweiMAC
 
 
class AbstractFactory(object):
    # 抽象的工厂类
    __metaclass__ = abc.ABCMeta
    # python不同于java没有abstract抽象类关键字通过加载abc实现抽象方法
    @abc.abstractmethod
    def get_phone(self):
        pass
 
    @abc.abstractmethod
    def get_computer(self):
        pass
 
 
# 苹果工厂
class IPhoneFactory(AbstractFactory):
    def get_phone(self):
        return IPhone()
    def get_computer(self):
        return IMAC()
 
 
# 华为工厂·
class HuaweiFactory(AbstractFactory):
    def get_phone(self):
        return Huawei()
    def get_computer(self):
        return HuaweiMAC()
 
if __name__ == '__main__':
    print IPhoneFactory().get_phone()
    print IPhoneFactory().get_computer()
    print HuaweiFactory().get_phone()
    print HuaweiFactory().get_computer()
