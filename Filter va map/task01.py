def filterlangan(lst):
    return list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), lst))

mx_lst = [1, "hello", 3.14, True, 42, "Python", 0, None]
num_lst = filterlangan(mx_lst)
print(num_lst)

#gpt dan ozro yordam oldm😅😅