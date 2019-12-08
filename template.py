#!/usr/bin/env
#encoding=utf-8
#模版方法模式
#ref:https://www.cnblogs.com/Xjng/p/4029522.html

__author__ = 'kevinlu1010@qq.com'
#模版方法模式的宗旨就是，所有重复的东西，即需要写两次以上的东西都放在一个模版里面（可以是父类，也可以是一个函数)
#this is a template, the difference of different guy is released in child class
class Student():
    def answer1(self):
        print '题目1：XXXXXX'
        print '%s的答案是：%s'%(self.name, self.get_answer1())
    def get_answer1(self):
        return 'A'
    def answer2(self):
        print '题目2：XXXXXX'
        print '%s的答案是：%s'%(self.name, self.get_answer2())
    def get_answer2(self):
        return 'A'

#父类定义一个公共的方法，然后子类重写这个方法来实现子类之间的差异化。
class StudentA(Student):

    def __init__(self):
        self.name = 'studentA'

    def get_answer1(self):
        return 'B'

    def get_answer2(self):
        return 'B'

class StudentB(Student):

    def __init__(self):
        self.name = 'studentA'

    def get_answer1(self):
        return 'C'

    def get_answer2(self):
        return 'D'

if __name__=='__main__':
    student_a=StudentA()
    student_a.answer1()
    student_a.answer2()
    student_b=StudentB()
    student_b.answer1()
    student_b.answer2()