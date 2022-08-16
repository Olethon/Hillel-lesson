elements = "64839447586679"
for index, element in enumerate(elements):
    if index != 0 and index != -1:
        if elements[index] > elements[index + 1] and elements[index] > elements[index - 1]:
            print(elements[index])
