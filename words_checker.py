para = input('请输入一段英文文本:')
words = para.split()
dictword = {}
for word in words:
    dictword[word] = dictword.get(word,0)+1

print(dictword)
