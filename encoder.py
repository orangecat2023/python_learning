data = input("请输入明文：")
for i in data:
    if "A" <= data <= "W":
        print(chr(ord(i)+3),end="")
    else:
        print(chr(ord(i)+3-26),end="")
