#!/usr/bin/env python
#encoding=utf-8
import logging
# one to one 

class Informer(object):
    observers = []

    def __init__(self):
        pass

    def register(self, observer):
        self.observers.append(observer)

    def notify(self):
        for ob in self.observers:
            ob.action()

class  Observer(object):
    
    def __init__(self, name):
        self.name = name

    def action(self):
        print("%s stop to play phones, come back to work" % self.name)


def main():
    ob1 = Observer("Mike")
    ob2 = Observer("Jack")

    informer = Informer()
    informer.register(ob1)
    informer.register(ob2)
    informer.notify()

if __name__ == '__main__':
    main()  

