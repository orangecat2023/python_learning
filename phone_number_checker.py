data = {'张三':'13309283335','李四':'18989227822','王五':'13382398921',
'林琦':'19833824743','薛伟':'18807317878','健全':'15093488129',
'吴鹏':'19282937665'}
while True:
    data_1 = input("请输入待查人员姓名：")
    if data.get(data_1,0) == 0 and data_1 != 'quit':
        print("该用户不存在")
    elif data.get(data_1,0) != 0 and data_1 != 'quit':
        print(data.get(data_1,0))
    elif data_1 == "quit":
        print("您已结束查询！")
        break
