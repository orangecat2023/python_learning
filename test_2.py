def comb(a,b):
    a_ge = a%10
    a_shi = (a - a_ge)/10
    b_ge = b%10
    b_shi = (b - b_ge)/10
    return 1000*a_ge+b_ge*100+a_shi*10+b_shi
data1,data2 = input().split(" ")
print(int(comb(int(data1),int(data2))))
