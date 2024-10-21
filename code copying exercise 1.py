with open("trans.in") as in_file:
    line = in_file.read()

line = line + '\n'
n_list = []
n_str = ''
for c in line:
    if c.isdigit():
        n_str += c
    else:
        if len(n_str) > 0:
            n_list.append(n_str)
            n_str = ''


with open("trans.out", "w") as out_file:
    out_file.write(str(len(n_list)) + '\n')
    for n in n_list:
        out_file.write(n + ' ')