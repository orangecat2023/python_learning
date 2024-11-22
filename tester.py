import sys
test_data = []
try:
    while True:
        line = input()
        test_data.append(line)
except EOFError:
    print("测试数据如下：")
    for line in test_data:
        print(line)
