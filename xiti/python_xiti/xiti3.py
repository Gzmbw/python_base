#coding=utf-8

"""
#读文件
#这里的文件名可以用文件的完整路径
f=file('data.txt') #这一步只是打开了一个文件，并没有得到其中的内容，变量f保存了这个文件还需要去读取它的内容，可以通过read()函数把文件内容读进一个字符串中。
data=f.read() #注意这里data是一个变量名，换成其他也可以，但是不能不写
print data
f.close()
#读文件内容的方法还有
#readline() 读取一行内容
#readlines() 把内容按行读取至一个list中

#写文件需要三步，打开文件，把内容写入文件，关闭文件。
foo=file('output.txt','w')
foo.write('a string you want to write haha')
foo.close()
"""
#注意这里的f,data,a都是变量。并且open()和file()的用法一样
"""
f=file('data.txt')
data=f.read() #把文件的内容存储到了变量data中
a=open('output.txt','w')
a.write(data)
a.close()
f.close()
"""
#从控制台输入一些内容，保存至一个文件
"""
data='I will be in a file.\nSo cool!'
a=open('output.txt','a')
a.write(data)
a.close()
"""

#统计每个学生的平时作业总的分
"""
#数据在scores.txt文件里
f=file('scores.txt')
lines=f.readlines()
f.close()
results=[]
for line in lines:
    data=line.split() #split()是分割函数，括号的参数是分割依据，不填是按照空格分割的
    sum=0
    for score in data[1:]:
        sum += int(score)
    result= '%s\t：%d\n'%(data[0],sum)
    results.append(result)

output=open('result.txt','w')
output.writelines(results) #注意这里要写入一个列表，所以要用writelines(),所以要分清你要添加的东西
output.close()
"""
#break和continue的区别
"""
i=0
while i<5:
    i += 1
    for j in range(3):
        print j
        if j==2:
            break
    for k in range(3):
        if k==2:
            continue
        print k
    if i>3:
        break
    print i
"""
#异常处理
#在python中，就可以使用try...except语句来处理异常，做法是把可能引发异常的语句放在try:块中，把处理异常的语句放在except:块
"""
try:
    f=file('non-exist.txt')
    print 'File opened!'
    f.close()
except:
    print 'File not exists.'
print 'Done'
"""
"""
score={
    'jian' : 98,
    'xiao' : 97,
    'lidan' : 87
}
for name in score:
    print '%s : %d'%(name,score[name]) #注意遍历的变量中存储的是字典的键
    print name , score[name]  #和上一行输出的形式有什么区别。如果光输出变量的值，就用这种输出形式如果输出不光是变量的值，还有其他要说的话，就采用上一行的输出形式
"""






