
elements = list(input("Введите элементы: "))
for index in range(1, len(elements), 2):
    elements[index-1], elements[index] = elements[index], elements[index - 1]
print(elements)