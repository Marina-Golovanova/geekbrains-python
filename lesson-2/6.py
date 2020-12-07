spisok = list()
index = 0
while True:
  name = input("Введите название товара: ")
  price = input("Введите цену товара: ")
  numbers = int(input("Введите кол-во товара: "))
  unit = input("Введите единицу измерения товара: ")
  good = {'name': name, 'price': price, 'numbers': numbers, 'unit': unit}
  index += 1
  spisok.append([index, good])
  print(spisok)
