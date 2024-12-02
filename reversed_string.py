with open("invertsub.in","r") as fp:
    data_original = fp.readlines()
    data1_t = data_original[0]
    data1 = data1_t.rstrip().rstrip('＃#') 
    data2_t = data_original[1]
    data2 = data2_t.rstrip().rstrip('＃#') 
result = data1.replace(data2, ''.join(reversed(data2)))
with open("invertsub.out","w+") as fp2:
    fp2.write(result)
