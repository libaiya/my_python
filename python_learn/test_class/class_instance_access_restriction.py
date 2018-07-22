#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年4月10日
@note: 类和实例，数据访问限制
面向对象（Objiect Orentied Programming）三大特征:
继承：子类重写父类方法
多态:父类引用指向子类对象
@author: pythonngeer
'''


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print "{0}'s score={1}".format(self.__name, self.__score)

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("type must be int")
        self.__score = score


if __name__ == '__main__':
    stu = Student('jack', 20)
#     print stu._Student__name
    stu.set_score(11)
    stu.print_score()
    stu.nickname = '杰克'
    print(stu.nickname)
    stu2 = Student('Tom', 21)
    # 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例
    print(stu2.nickname)
