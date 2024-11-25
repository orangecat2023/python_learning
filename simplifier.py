from fractions import Fraction
data1,data2 = input().split()
data3 = Fraction(int(data1),int(data2))
print(data3.numerator,data3.denominator)
