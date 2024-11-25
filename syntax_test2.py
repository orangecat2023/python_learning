def info(city):
        print('在函数中被赋值前：', id(city), city)
        city = '青岛' #局部变量退出程序后即消失
        print('在函数中被赋值后：', id(city), city)
 
mycity = '北京'
print('函数被调用前：', id(mycity), mycity)
info(mycity)  
print('函数被调用后：', id(mycity), mycity)
