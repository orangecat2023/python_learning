s = input("请输入由大小写字母组成的字符串：")
n = 0
#定义n为计数器变量
for c in s:
    if c  in  'aeiouAEIOU':
        n += 1
print(n)
