a = int(input("Введіть А:"))
b = int(input("Введіть B:"))
if a < b:
    print(list(range(a, b+1)))
if a > b:
    print(list(range(a, b-1, -1)))
