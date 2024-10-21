data = 0
agree_amount = 0
disagree_amount = 0
flag = True
while flag:
    data = input()
    if data == "1":
        agree_amount += 1
    elif data == "0":
        disagree_amount += 1
    elif data == "-1":
        flag = False
total_people_amount = agree_amount + disagree_amount
agree_rate = round(agree_amount/total_people_amount,3)
if agree_rate >= 0.5:
    print("Yes")
elif agree_rate < 0.5:
    print("No")
