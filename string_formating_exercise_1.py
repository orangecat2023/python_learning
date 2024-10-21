first, second = input().split()
first = float(first)
second = float(second)


total = first + 0.9 * second
print ("%16.2f" % first)
print ("%16.2f" % (second * 0.9))
print("-" * 16)
print ("Total:" + "%10.2f" % total)
