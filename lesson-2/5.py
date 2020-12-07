my_list = [7, 5, 3, 3, 2]
while True:
  el = int(input("Введите элемент рейтинга: "))
  my_list.append(el)
  my_list.sort(reverse=True)
  print(my_list)