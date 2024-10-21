n = int(input("请输入n"))
if n%100 != 0:
    print("输入错误！")
else:
        result = 0
        for n2 in range(n//2+1):
            
            for n5 in range(n//5+1):
                for n10 in range(n//10+1):
                    if n2*2+n5*5+n10*10 == n:
                        result += 1
        print(result)
