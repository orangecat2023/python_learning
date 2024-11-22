db = {}
while True:
    data = input('请输入词语及对应的释义：')
    if data == "q" or data == "Q":
        break
    else:
        meme,meaning = data.split()
        db[meme] = meaning
for meme_1 in db.keys():
    print(meme_1+":"+db[meme_1])
