languages = {'张三' : 'python', '李四': 'c', '王五' : 'python', '钱六' : 'java' }
friends = ['张三', '钱六', '阮小二']
for friend in friends:
    if friend in languages.keys():
        print('嗨'+friend+'，我看到你喜欢的编程语言是'+languages[friend].title())
