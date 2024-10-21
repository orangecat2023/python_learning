a=int(input("请输入三位整数："))
b=a%100
digits=a%100%10
tens=(b-digits)//10
hundreds=int((a-digits-tens*10)/100)
print("百位数字为",hundreds,"十位数字为",tens,"个位数字为",digits)
