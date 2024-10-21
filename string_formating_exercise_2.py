name = input("请输入英文名称：")
if name.isalpha() == True:
    print("您的姓名是"+name.capitalize())
else:
    print("您输入的姓名不是字母")

age = input("请输入您的年龄：")
if age.isdigit() == True:
    print("您的年龄是"+age+"岁")

else:
    print("您输入的不是数字")
