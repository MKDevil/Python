#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Animal(object):
    def reply(self):
        self.speak()


class Mammal(Animal):
    def speak(self):
        print('Mammal!')


class Cat(Mammal):
    def speak(self):
        print('meow')


class Dog(Mammal):
    def speak(self):
        print('wong')


class Primate(Mammal):
    def speak(self):
        print('Hello world!')


class Hacker(Primate):
    pass
