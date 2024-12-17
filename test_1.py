data = int(input())
step_data = 1
result = 1
for i in range(2,data+1):
    step_data += i
    result += 1/step_data
print('{:.4f}'.format(result))
    
    
