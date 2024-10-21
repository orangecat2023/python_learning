import random
mine_Row, mine_Column = random.randint(1, 6), random.randint(1, 6)  #由随机数生成地雷所在的行号和列号
print(mine_Row, mine_Column)

for i in range(6):  #输出#输出扫雷区：一个6*6的图案（对应位置上的图案为○）
    for j in range(6):
        print('○', end = '')
    print()
    
p = [[1 for o in range(6)] for o in range(6)]#生成二维数组，每个元素均为1
p[mine_Row-1][mine_Column-1] = 0   #用地雷所在的行号和列号将p对应位置上的数字置为0
n = 0  #用来统计挖雷步数
#print(p)

while True:
    try:  #通过异常机制控制输入非法数据的情况，如hi
        row, column = map(int, input('请输入你的选择(行 列):').split())
        n += 1 #计数变量加1
        
        if p[row-1][column-1] == 0:  #挖中雷
            print('you win\n一共走了{}步'.format(n))
            break
        else:
            print('选择后：')
            p[row-1][column-1] = 2  #将对应位置置为2，以示区别 
            
            for i in range(6): #输出扫雷区,如果行、列号与与p中取值为2的行列号相同，则将此位置上的图案由○置为●  
                for j in range(6):
                    if p[i][j] == 2: 
                        print('●', end = '')  
                    else:
                        print('○', end = '')
                print()
    except:
        print('输入有误，请重新输入')
