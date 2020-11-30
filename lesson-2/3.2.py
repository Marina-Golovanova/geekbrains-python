month = int(input("Введите номер месяца: "))
seasons = dict(
  Winter = [12, 1, 2],
  Spring = [3, 4, 5],
  Summer = [6, 7, 8],
  Fall = [9, 10, 11]
)

for index in range(len(list(seasons.keys()))):
  for el in list(seasons.values())[index]:
    if el == month:
      print(list(seasons.keys())[index])