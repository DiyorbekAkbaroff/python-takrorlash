intp = input()

s = lambda a: ''.join(filter(lambda c: c.isdigit(), a))
print(s(intp))