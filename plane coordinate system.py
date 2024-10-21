data = input()
x,y = data.split()
x=float(x)
y=float(y)
if x == 0 and y == 0:
    print(0)
elif x == 0 and y != 0:
    print("y")
elif y == 0 and x != 0:
    print("x")
elif x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y < 0:
    print(3)
elif x < 0 and y > 0:
    print(2)