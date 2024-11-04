#to record my cats
heihei = {'颜色' : '黑白', '尺码' : '肥胖', '生日' : '2018.09'}
juju = {'颜色' : '橘色', '尺码' :'肥胖', '生日' : '2019.07'}
huihui = {'颜色' : '灰色', '尺码' : '正常', '生日' : '2020.08'}

l = [heihei, juju, huihui]
count = 1

for cat in l:
    print('cat'+ str(count), end = '---')
    count += 1
    
    for k, v in cat.items():
        print(k + ':'+ v, end = ';')
    print()
