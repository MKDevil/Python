#!/usr/bin/env python
# -*- coding:utf-8 -*-
import person
import shelve
bob = person.Person('Bob Smith')
sue = person.Person('Sue Jones', 'dev', 3500)
tom = person.Manager('Tom Jones', 4500)

with shelve.open('persondb') as db:
    for object in (bob, sue, tom):
        db[object.name] = object
    del db['Bob Smith']

with shelve.open('persondb') as db:
    for key in db:
        print(key, ' => ', db[key])
