n = int(input())
a1 = 1
a2 = 1
for i in range(2,n+1):
    a2 = a2+i
    a1 = a1 + 1/a2
print('%.4f'% a1)

