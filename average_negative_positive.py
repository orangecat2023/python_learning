positive = 0
ls = []
negative = 0
while True:
    data = input()
    if data == '0':
        break
    else:
        data = int(data)
        ls.append(data)
        if data<0:
            negative += 1
        if data>0:
            positive += 1

average = float(sum(ls)/len(ls))
print('%.2f'% average)
print(positive)
print(negative)
