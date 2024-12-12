data = list(input())
pairing_ls = ["1","0","X","9","8","7","6","5","4","3","2"]
sum = int(data[0])*7+int(data[1])*9+int(data[2])*10+int(data[3])*5+int(data[4])*8+int(data[5])*4+int(data[6])*2+int(data[7])+int(data[8])*6+int(data[9])*3+int(data[10])*7+int(data[11])*9+int(data[12])*10+int(data[13])*5+int(data[14])*8+int(data[15])*4+int(data[16])*2
remain_order = sum % 11
if pairing_ls[remain_order] == str(data[17]):
    print("YES")
else:
    print("NO")
