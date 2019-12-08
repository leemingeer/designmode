#!/usr/bin/env python
#many to many
#encoding=utf-8

__author__ = 'leemingeer'
from abc import ABCMeta, abstractmethod

#all the informers has the same attributes, this can forms a class
class Subject():
    __metaclass__ = ABCMeta
    observers=[]
    status=''
    @abstractmethod
    def attach(self,observer):
        pass
    @abstractmethod
    def detach(self,observer):
        pass
    @abstractmethod
    def notify(self):
        pass


#all the observer has the same name and subscribe: boss class
class Observer():
    __metaclass__ = ABCMeta
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
    @abstractmethod
    def update(self):
        pass


class Boss(Subject):
    def __init__(self):
        pass
    def attach(self,observer):
        self.observers.append(observer)

    def detach(self,observer):
        self.observers.remove(observer)
    def notify(self):
        for observer in self.observers:
            observer.update()

class BA(Subject):
    def __init__(self):
        pass
    def attach(self,observer):
        self.observers.append(observer)

    def detach(self,observer):
        self.observers.remove(observer)
    def notify(self):
        for observer in self.observers:
            observer.update()


class StockObserver(Observer):
    def update(self):
        print '%s,%s停止看股票'%(self.sub.status,self.name)
class NBAObserver(Observer):
    def update(self):
        print '%s,%s停止看NBA'%(self.sub.status,self.name)


if __name__=='__main__':    
    boss=Boss()
    observe1=StockObserver('张三',boss)
    observe2=NBAObserver('李四',boss)
    boss.attach(observe1)
    boss.attach(observe2)
    #boss.detach(observe2)
    boss.status='我是老板，我来了'
    #boss.notify()

    ba=BA()
    observe1=StockObserver('张三',ba)
    observe2=NBAObserver('李四',ba)
    ba.attach(observe1)
    ba.attach(observe2)
    #ba.detach(observe2)
    ba.status='我是ba，我来了'
    #boss.notify()
    ba.notify()