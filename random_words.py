from random import *
#定义3个列表保存不同的词
roles = ['哆啦A梦', '奥特曼', '苏大强', '容嬷嬷', '甄嬛', '谢耳朵', '谷爱凌']
spots = ['埃菲尔铁塔上', '地铁上大街上', '飞机上', '三里屯', '浴室里', '王者峡谷', '宾馆里', '珠穆朗玛上']
events = ['背课文', '高唱《死了都要爱》', '蹦极', '补暑假作业', '开黑 800米跑', '滑雪', '期末考试']
for i in range(1,10):
    print(choice(roles)+"在"+choice(spots)+choice(events))
