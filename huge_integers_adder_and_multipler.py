with open('plus.in','r') as orct:
    data_ls = orct.readlines()
for i in range(len(data_ls)):
    data_ls[i] = data_ls[i].strip('\n')
a = int(data_ls[0])
b = int(data_ls[2])
method = data_ls[1]
if method == '+':
    result = a+b
elif method == '*':
    result = a*b
with open('plus.out','w') as orct_1:
    orct_1.write(str(result))
