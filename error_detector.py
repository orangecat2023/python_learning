try:
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = int(input("请输入一个整数: "))     #索引不应超过字符串长度-1
    print(s[i])
except ValueError:
    print("输入类型错误，请输入一个整数!")
except IndexError:   #也可以直接使用except，指出除了上面的ValueError，其他错误均执行下面的语句
    print("索引错误")
