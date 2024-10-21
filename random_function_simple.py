import random
sig = random.randint(0, 2)
if sig == 0:
    print("红灯，停！")
elif sig == 1:
    print("绿灯，行")
else:
    print("黄灯，注意")
