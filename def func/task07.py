son = [4,1,2,1,2]

a = len(list(filter(lambda x: a.count(x) == 1, son)))
b = list(filter(lambda x: a.count(x) == 1, son))

print(a, " --> ", b)