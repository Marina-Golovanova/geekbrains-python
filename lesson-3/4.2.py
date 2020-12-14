def my_func(x, y):
  """Возвращает число возведенное в степень

  Параметры:
  x - число
  y - степень

  """
  result = 1
  try:
    if x > 0 and y < 0:
      for i in range(0, y, -1):
        result = result / x
      return result
  except ValueError:
    return
