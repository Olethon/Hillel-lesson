x = float(input("Введіть початкову відстань:"))
y = float(input("Введіть кінцеву відстань:"))
day = 0
while True:
    x = x + x * 0.1
    day += 1
    if x > y:
        break
print("День:", day)
