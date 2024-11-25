def simplifier(a,b):
    for i in range(2,(max(a,b)-1)):
        if a%i + b%i == 0:
            a = a/i
            b = b/i
    return int(a),int(b)
data1,data2 = input().split()
data1,data2 = map(int,simplifier(int(data1),int(data2)))
m,n = map(int,simplifier(int(data1),int(data2)))
print(m,n)      
