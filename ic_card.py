ic_number = input("请输入十八位身份证号码:")
if len(ic_number) != 18:
    print("身份证号码长度有误")
else:
    print("此人所在地代码为",ic_number[0:6])
    print("生日：",ic_number[6:10],"年",ic_number[10:12],"月",ic_number[12:14],"日")
    if float(int(ic_number[16])/2).is_integer == True:
        print("性别：女")
    else:
        print("性别：男")
