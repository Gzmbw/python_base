#coding=utf-8
# 1第一次只是从文件读取数据但是没有保存数据
"""
from random import randint
#读取文件中的成绩数据
f=open ('game1.txt') #注意文件路径
score=f.read().split()
#分别存入变量中
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
#计算游戏的平均轮数，注意浮点数和避免除零错误
if game_times >0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0
#输出成绩信息，平均轮数保留2位小数
print '你已经玩了%d次，最少%d轮猜出答案，平均%0.2f轮猜出答案' %(game_times,
     min_times,avg_times)
#因为这行代码太长，在括号后换行，注意并不是所有位置都可以换行

num = randint(1,100)
print 'Guess what I think?'
bingo = False
while bingo == False:
    answer = input()
    if answer < num:
        print 'too small!'
    if answer > num:
        print 'too big!'
    if answer == num:
        print 'BINGO!'
        bingo = True
"""
#2我们要把每次游戏结果保存进取
#但是只有一组数据，不管谁玩都会算在里面,下面在改进
"""
from random import randint

f=open('game1.txt')
score=f.read().split()
f.close()
game_times= int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0
print '你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' %(game_times,min_times,avg_times)
num = randint(1,100)
times = 0 #记录本次游戏轮数
print 'Guess what I think?'
bingo = False
while bingo==False:
    times += 1
    answer = input()
    if answer < num:
        print 'too small!'
    if answer > num:
        print 'too big!'
    if answer == num:
        print 'BINGO!'
        bingo=True

#如果是第一次玩，或者论数比最小轮数少，则更新最小轮数
if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
result = '%d %d %d '%(game_times,min_times,total_times) #用一个变量来记录数据，这里的result是字符串
f=open('game1.txt','w')
f.write(result)
f.close()
"""

#进一步改进，玩家需要做的是，在游戏开始前，输入自己的名字，根据这个名字记录他的成绩
