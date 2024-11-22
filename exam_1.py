data = list(input().split(" "))
data_real = list([])
st = set({})
for i in data:
    result = float(i)
    data_real.append(result)
max_num = max(data_real)
for i in range(len(data_real)):
    st.add(data_real.index(max_num,i))
for i in st:
    print(i+1,end=' ')
