import random
lst = [random.randint(0,100) for i in range(1000)]
d = set(lst)
for v in d:
    print(v,":",lst.count(v))
