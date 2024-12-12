ls=[]
with open('课堂活动13.csv','r') as fr:
    ls = [line.strip().split(',') for line in fr]

ls.pop(0)
for i in range(len(ls)):
    if int((ls[i])[2])>170 and int((ls[i])[3])<=50:
        print((ls[i])[0])
