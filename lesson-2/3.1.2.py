seasons = ("Зима", 12, 1, 2, "Весна", 3, 4, 5, "Лето", 6, 7, 8, "Осень", 9, 10, 11)
while True:
  month = int(input("Введите номер месяца: "))
  if month < 1 or month > 12:
    print("Вы ввели неправильное число!")
    continue
  else:
    index_month = seasons.index(month)
    while type(seasons[index_month - 1]) != str:
      index_month -= 1
    print(seasons[index_month - 1])
    break
