running = True
while running:
    numbers = input("Введіть трицифрове число:")
    if len(numbers) == 3:
        print(f"Загальна сумма цифр: {sum([int(num) for num in numbers])}")
        running = False

