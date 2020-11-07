_list = input().split()
n_l = []
for i in _list:
    f = i.split('.')
    f[0] = f[0].rjust(3, '0')
    f = '.'.join(f)
    n_l.append(f)
print(n_l)




