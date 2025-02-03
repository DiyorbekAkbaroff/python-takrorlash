fltr = lambda n: next((x for x in range(n + 1) if x * x == n), -1)

n = int(input("N sonini kiriting: "))

result = fltr(n)
print(result)