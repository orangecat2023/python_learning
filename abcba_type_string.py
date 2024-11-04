data = input()
if len(data) > 50:
    print("长度过长！")
else:
    data = list(data)
    data_a = list(reversed(data))
    if data == data_a:
        print("Yes")
    else:
        print("No")
