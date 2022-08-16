import math
user_input = None
element_to_operate = []
while user_input != 0:
    user_input = int(input("Введіть число:"))
    element_to_operate.append(user_input)
print("Кількість введених чисел:", len(element_to_operate[:-1]))
print("Сумма введених чисел:", sum(element_to_operate))
print("Добуток введених чисел:", math.prod(element_to_operate[:-1]))
print("Середнє арифметичне:", sum(element_to_operate)/len(element_to_operate[:-1]))
print("Найбільше число:", max(element_to_operate))
print("Порядковий номер найбільшого числа :", element_to_operate.index(max(element_to_operate)) + 1)
print("Кількість парних чисел:", len([elem for elem in element_to_operate if elem % 2 == 0]))
print("Кількість непарних чисел:", len([elem for elem in element_to_operate if elem % 2 != 0]))
second_max_elements = [elem for elem in element_to_operate if elem != max(element_to_operate)]
print("Значення другого за величиною елемента цієї послідовності", max(second_max_elements))
max_elements = [elem for elem in element_to_operate if elem == max(element_to_operate)]
print("Кількість найбільших чисел:", len(max_elements))



