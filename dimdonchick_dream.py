data_temp, data_except = [], []
while True:
    try:
        t = float(input("请输入体温值(0表示结束输入)："))
        if t != 0:
            if 35<= t <= 42:
                data_temp.append(t)
            else:
                print('温度越界，请重新输入')
        else:
            break
    except:
        print('输入有误，请输入数值')

for data in data_temp:  
    if data >= 38:
        data_except.append(data)

print('共有{}个异常数据'.format(len(data_except)))
for i in data_except:
    print(i, end = ' ')
