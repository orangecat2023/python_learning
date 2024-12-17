with open("text1.dat",'r') as orct:
    a = orct.readlines()
for i in range(len(a)):
    a[i] = a[i].strip("\n")
    a[i] = (a[i])[::-1]
with open('text2.dat','w') as orct2:
    for i_1 in a:
        orct2.writelines(i_1+"\n")
