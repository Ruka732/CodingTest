a = [['X'], ['X', 'b'], ['c']]

b = list(filter(lambda x: a[x] == 'X', range(len(a))))
c = a[0].index('b')
print(c)