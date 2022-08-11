import random
rnd = random.randint(1, 10)
chance = 0
while chance != 3:
    numeric = int(input("Вгадай число від 1 до 10:"))
    if numeric == rnd:
        print("You won!")
        break
    if numeric != rnd:
        print("You lose!")
        chance += 1
        if chance == 3:
            print(f"Спроби завершились, задане число було {rnd}")

