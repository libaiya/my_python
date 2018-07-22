#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年5月14日

@author: 'lxq'
'''


class Animal(object):
    def run(self):
        print("animal is running")


class Dog(Animal):
    def run(self):
        print("Dog is running")


class Cat(Animal):
    def run(self):
        print("Cat is running")


class Person(object):
    def run(self):
        print("Person is running")


def runTwice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    d = Dog()
    d.run()
    p = Person()
    runTwice(d)
    runTwice(p)
