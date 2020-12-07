
while True:
  month = int(input("Введите номер месяца: "))
  seasons = ('Зима', 'Весна', 'Лето', 'Осень')
  if month < 1 or month > 12:
    continue
  elif month in range(1, 2) or month == 12:
    print(seasons[0])
    break
  elif month in range(3, 5):
    print(seasons[1])
    break
  elif month in range(6, 8):
    print(seasons[2])
    break
  else:
    print(seasons[3])
    break