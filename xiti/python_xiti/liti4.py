#coding=utf-8

#函数的默认参数
def hello(name):
    print 'hello '+ name
hello('world')

#如果很多时候，都用world来调用这个函数，少数情况才会去改变参数，那么就可以给这个函数一个默认参数

def f(name='world'):
    print 'hello '+name
f()#当你没有提供参数值时，这个参数就会使用默认值，如果你提供了，就用你给的。
f('python')
#注意，当函数有多个参数时，如果你想给部分参数提供默认参数，那么这些参数必须在参数的末尾
def func(a,b=5):
    print a+b
func(2)
