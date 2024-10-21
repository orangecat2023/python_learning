period = float(input("请输入工作年限："))
salary = float(input("请输入月薪:"))
if 1 > period > 0:
    if salary <= 8000:
        ratio = 1
    else:
        ratio = 1.2
elif 2 > period >= 1:
    if salary <= 10000:
        ratio = 1.7
    else:
        ratio = 1.5
else:
    if salary <= 12000:
        ratio = 3
    else:
        ratio = 3.2

year_reward = ratio * salary
result = str(year_reward)
print("你的年终奖金额为"+result+"元")
