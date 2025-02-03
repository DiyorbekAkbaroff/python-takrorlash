def lst( a ):
    son = int("".join(map(str, a)))
    son += 1
    return list(map(int, str(son)))

print(lst([1,2,3]))
print(lst([9]))
print(lst([9,9,9,9]))