 #coding: utf-8 

"""
Spyder Editor

This is a temporary script file.
"""
'''
from random import randint
num = randint(1,100)
bingo=False
while bingo!=True:
    i=input()
    if i<num:
        print '%d is too small.' %i
    if i>num:
        print '%d is too big.' %i
    if i==num:
        print '%d is the right answer!' %i
        bingo=True

for i in range(0,5):
    print '* * * * *'
'''
for i in range(0,5):
    for j in range(0,i+1):
        print '*',
    print