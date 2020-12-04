def my_func():
  """Возвращает сумму наибольших двух аргументов"""
  var_1 = int(input("Введите число 1: "))
  var_2 = int(input("Введите число 2: "))
  var_3 = int(input("Введите число 3: "))
  arr = [var_1, var_2, var_3]
  max_1 = arr.pop(arr.index(max(arr)))
  max_2 = arr.pop(arr.index(max(arr)))
  return f"Сумма наибольших двух аргументов: {max_1 + max_2}"

print(my_func())