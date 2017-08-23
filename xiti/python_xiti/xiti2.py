# coding=utf-8
"""
#第一个例题
def isEqule(num1,num2):
    if num1<num2:
        print "too small"
        return False
    if num1==num2:
        print "bingo"
        return True
    if num1>num2:
        print "too big"
        return False

from random import randint
num=randint(1,100)
print "Guess what i think?"
bingo=False
while bingo==False:
    answer=input()
    bingo=isEqule(answer,num)
"""

"""
x=input()#第二个例题，if的嵌套
y=input()
if x>=0:
    if y>=0:
        print 1
    else:
        print 4
elif x<0:
    if y>=0:
        print 2
    else:
        print 3
"""
"""
print range(1,10)#直接输出一个列表
l=range(1,10)
for i in l:#for循环做的事情就是遍历一个列表中的每一项，每次循环都把当前项赋值给一个变量，这里是i，直到列表结束
    print i,
print

l=[1,2,3,4,5]#同样可以用for..in遍历这个列表，依次输出了列表中的每一项
for i in l:
    print i,
print
print l
#列表中的元素可以是不同类型的组合
l=['meat','egg','fish','milk']
print l
l=[365,'everyday',0.618,True]
print l
print l[1]
#修改list中的某个元素，只需要直接给那个元素赋值就可以
l[0]=123
print l
l.append(1024)#添加一个元素
print l
del l[0]#删除某个元素
print l
"""

"""
#list有两类常用的操作：索引(index)和切片(slice)
#索引可以是负数；切片操作符是在[]内提供一对可选的数字，用：号分割。冒号前的数表示切片的开始位置，冒号后的的数字表示到那里结束。
l=[365,'everyday',0.628,True]
a=l[1:3]
b=l[:]
print a
print b
c=l[0:-3]
print c
print l[1:3]
print l#注意l是没有变化的












