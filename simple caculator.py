data = input()
int1,int2,op = data.split()
int1 = int(int1)
int2 = int(int2)
if op == "+":
    result = int1+int2
    print(int(result))
elif op == "-":
    result = int1 - int2
    print(int(result))
elif op == "*":
    result = int1 * int2
    print(int(result))
elif op == "/":
    result = int1 / int2
    if result.is_integer() == True:
        print(int(result))
    else:
        print('%.2f'% result)

    