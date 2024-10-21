from math import pi
radius = input("请输入圆的半径：")
radius = float(radius)
cir = 2*pi*radius
area = pi*radius*radius
cir = '%.2f'% cir
area = '%.2f'% area
print("圆的周长是",cir,"圆的面积是",area)
