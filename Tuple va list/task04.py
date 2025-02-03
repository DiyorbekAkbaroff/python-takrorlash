a = list(input("Kop son kiriting"))

son = 0

for i in a:
    if a.count(i) == 1:
        son += 1
        print(i)
        
print(son)