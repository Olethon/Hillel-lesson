set_1 = set(range(0, 101, 10))
set_2 = set(range(0, 91, 9))
print(sorted(set_1))
print(sorted(set_2))
print(sorted(set_1.intersection(set_2)))
print(sorted(set_1.difference(set_2)))
print(sorted((set_1 | set_2) - (set_1 & set_2)))


