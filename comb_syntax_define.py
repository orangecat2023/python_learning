def comb(a,b):
    k = a%10
    h = b%10
    t = (a-(a%10))/10
    s = (b-(b%10))/10
    return k*1000+h*100+t*10+s
data1,data2 = input().split()
data1 = int(data1)
data2 = int(data2)
print(int(comb(data1,data2)))
