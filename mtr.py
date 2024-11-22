mtx = []
for r in range(4):
    mtx.append(list(map(float,  input().split())))
avg_r = []
for r in range(4):#逐一访问各行
    avg_r.append(sum(mtx[r]) /len(mtx[r]))

for v in avg_r:
    print(v, end=' ')
