a = [1, 2, 3, 5, 7, 8, 9, 10]

flt = lambda x: {"toq": len(list(filter(lambda s: s % 2 != 0, x))), "juft": len(list(filter(lambda s: s % 2 == 0, x)))}

print(flt(a))
