times = 1
a_list = []
while True:
    if times <= 10 :
        try:
            score_input = int(input("请输入第"+str(times)+"位评委的打分:"))
            if 0 <= score_input <= 10:
                a_list.append(score_input)
                times += 1
            else:
                print("输入的数值越界！")
        except ValueError:
            print("输入的不是数值，请重新输入！")
    if times > 10:
        break
a_list.sort()
a_list.pop()
a_list.pop(0)
print(a_list)
print("平均值为"+str((sum(a_list)/len(a_list)))+"分")
    
        
