data = input()
if data.isdigit() == True and len(data) == 3:
    data = data[::-1].strip('0')
    print(data)
else:
    print("-1")
