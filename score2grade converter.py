score = int(input("输入百分制成绩:")) 
degree = ‘DCBAAF’ #字符串类型，可通过[index]索引

if score >  [填空1]  or score <  [填空2] : #如果成绩超界，则输出有误信息；请填写整数
    print("输入有误")
else:
    index = (score -  [填空3] )//10  #将不同范围的成绩划归到有限情况（0|1|2|3|4|其他）
    if index >= 0:
        print(degree[index])  #与表示分数等级的字符串关联，输出及格成绩对应的等级
    else:
        print(degree[ [填空4] ]) #输出不及格成绩对应的等级