a = [1, 2, 33, 5, 6, 7, 7]

son = int(input("Son kiriting = "))

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == son:
            print(i,",",j)