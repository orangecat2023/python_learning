data_inputed = input()
flag_overall = True
try:
    data_inputed = float(data_inputed)
except ValueError:
    flag_overall = False
try:
    if int(data_inputed) != data_inputed or (data_inputed.is_integer == True and int(data_inputed)<0):
        flag_overall = False
except AttributeError:
    flag_overall = False
if flag_overall == False:
    print("illegal input")
else:
    ls = []
    with open("in.txt",'r') as orct:
        for i in range(int(data_inputed)):
            data1 = orct.readline()
            ls.append(data1)
    counter = 0
    for i_1 in ls:
        if i_1[0] == "A":
            print(i_1.strip())
            counter += 1
    if counter == 0:
        print('not found')
            
