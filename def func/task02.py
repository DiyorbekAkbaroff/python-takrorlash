a = [1,2,3,4,5,6,7,8,9,10]

swaps = lambda lst: [lst[0], lst[-1], lst[2], lst[-2], lst[4], lst[5], lst[6], lst[3], lst[8], lst[1]]
print(swaps(a))