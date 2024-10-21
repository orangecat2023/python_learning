age=int(input("请输入你的年龄："))
if age <= 4:
    print("免费")
elif 4 <= age < 17:
    print("10元")
elif 18 <= age < 59:
    print("20元")
else:
    print("免费")
