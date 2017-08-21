#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:54:29 2017

@author: guo
"""

'''
for i in range(0,5):
    for j in range(0,i+1):
        print'*',
    print

print '%s is easy to learn ' %'python'

print '''
#%s's score is %d
''' % ('mike',87)
name='jianguo'
score=87
print "%s's score is %d" % (name,score)


a=1
print a
a='hello'
print a
a=True 
print a

a=12
b=str(a)
print b
type(b)



print bool('False')


a="123"
if a:
    print "this is not a blank string"

for i in range(1,11):
    for j in range(1,i):
        print i,j

name=input()
print name
name=raw_input()
print name
'''
def sayhello():
    print 'hello world!'
sayhello()

def sayhello(someone):
    print someone + 'sayhello'
sayhello(input())
def fun(a,b):
    print a+b
fun(1,2)