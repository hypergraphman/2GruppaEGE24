def f(n):
    s1 = bin(n)[2:]
    s2 = s1[1:]
    return int(s2, 2)


# print(f(131))
my_set = set()
for n in range(131, 3131 + 1):
    my_set.add(n - f(n))
print(my_set)
print(len(my_set))