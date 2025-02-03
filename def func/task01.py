def dicts(n):
    result = {}
    for item in n:
        key = item[0]
        value = item[1:]
        result[key] = value
    return result

i = [
    [1, "Jean Castro", "V"],
    [2, "Lula Powell", "V"],
    [3, "Brian Howell", "VI"],
    [4, "Lynne Foster", "VI"],
    [5, "Zachary Simon", "VII"],
]
a = dicts(i)

print(a)