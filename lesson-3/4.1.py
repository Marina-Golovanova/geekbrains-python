def my_func(x, y):
  """Возвращает число возведенное в степень

  Параметры:
  x - число
  y - степень

  """
  try:
    if x > 0 and y < 0:
      return x**y
  except ValueError:
    return
