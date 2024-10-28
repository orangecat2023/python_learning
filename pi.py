from random import *
from math import sqrt
from time import perf_counter
DARTS = pow(2,25)
hits = 0
perf_counter()#在第一次调用的时候，返回的是程序运行的实际时间
for i in range(1, DARTS+1):
    x, y = random(),random()                                 #产生两个随机小数
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1:
        hits += 1
pi = 4 * (hits/DARTS)
print("Pi值是{}.".format(pi))
print("运行时间是: {:5.5}s".format(perf_counter()))#以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔
