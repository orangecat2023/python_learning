try:
    data1 = input()
    data2 = input()
    data3 = input()
    data4 = input()
except EOFError:
    if data1 == '0':
        data4 = data3
        data3 = data2
        data2 = " "
        data1 = []
    elif data3 == '0':
        data3 = []
        data4 = " "
data2 = data2.split()
data4 = data4.split()
list1 = []
data2_new = []
data4_new = []
for i_3 in data2:
    data2_new.append(int(i_3))
for i_4 in data4:
    data4_new.append(int(i_4))
for i in data2_new:
    list1.append(i)
for i_1 in data4_new:
    list1.append(i_1)
result = sorted(list1)
for i_2 in range(len(result)-1):
    print(result[i_2],end=' ')
print(result[len(result)-1])
