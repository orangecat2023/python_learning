from random import *
time,a,b,flag = 0,0,0,1
while flag:
    result = randint(0,1)
    time += 1
    if result == 0:
        a += 1
    if result == 1:
        b += 1
    if time == 100:
        flag = False
print("正面的概率为:",a/time,";反面的概率为",b/time)
