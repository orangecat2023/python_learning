amount = input()
ls_data = input().split()
for i in range(len(ls_data)):
    ls_data[i] = float(ls_data[i])
ls_data = sorted(ls_data)
highest = '{:.1f}'.format(ls_data[len(ls_data)-1])
lowest = '{:.1f}'.format(ls_data[0])
aver = '{:.1f}'.format(sum(ls_data)/len(ls_data))
print(highest)
print(lowest)
print(aver)
