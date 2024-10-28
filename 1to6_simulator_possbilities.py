from random import *
time,flag,a,b,c,d,e,f = 0,1,0,0,0,0,0,0
while flag:
    time += 1
    random_result = randint(1,6)
    if random_result == 1:
        a += 1
    if random_result == 2:
        b += 1
    if random_result == 3:
        c += 1
    if random_result == 4:
        d += 1
    if random_result == 5:
        e += 1
    if random_result == 6:
        f += 1
    if time == 100:
        flag = False
print("六面的概率分别为:",a/time,b/time,c/time,d/time,e/time,f/time)
