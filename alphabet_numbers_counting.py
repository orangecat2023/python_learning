data=input()
number_amount = 0
alphabet_amount = 0
for i in data:
    if i.isdigit() == True:
        number_amount += 1
    elif i.encode().isalpha() == True:
        alphabet_amount += 1

print(str(alphabet_amount)+" "+str(number_amount))
