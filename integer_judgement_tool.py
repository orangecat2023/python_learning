s = input()
s=s.strip()
table = list(s)
if table[0] == "-" and s[1:].isdigit() or s.isdigit():
    print("yes")
else:
    print("no")

