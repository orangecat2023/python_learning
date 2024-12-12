flag = True
try:
    with open("in.txt",'r') as op1:
        data_ls = op1.readlines()
    if float(data_ls[0]).is_integer == True:
        data_ls.pop(0)
    else:
        flag = False
        
    data_ls_optimized = [float(i) for i in data_ls]
    for i_2 in data_ls_optimized:
        if i_2.is_integer() == True:
            flag = True
        else:
            flag = False
            break
    sorted_data = sorted(data_ls_optimized)
    with open('out.dat','w') as op2:
        if flag == False:
            op2.write("illegal input")
        else:
            for i_3 in sorted_data:
                op2.write(str(int(i_3))+'\n')
except ValueError:
    with open('out.dat','w') as op3:
        op3.write("illegal input")
    
