data = input()
data1,data2 = data.split(" ")
data3 = int(data1[::-1].strip("0"))
data4 = int(data2[::-1].strip("0"))
if data3 * data4 == int(data2) * int(data1):
    print(data1,"*",data2,"=",data3,"*",data4,sep='')
else:
    print(data1,"*",data2,"!=",data3,"*",data4,sep='')


