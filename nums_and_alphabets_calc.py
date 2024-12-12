data = input()
num_a = 0
num_n = 0
for i in data:
    if i.isdigit() == True:
        num_n += 1
    if i.isalpha() == True:
        num_a += 1
print(num_a,end = ' ')
print(num_n)
