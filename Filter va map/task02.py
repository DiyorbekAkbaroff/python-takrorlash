def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filterlangan(lst):
    return list(filter(is_prime, lst))

ages = [5, 12, 17, 18, 24, 32, 19, 0, 21]
yoshlari = filterlangan(ages)
print(yoshlari)

#Bunga ham ozro
