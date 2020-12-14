def division():
  """Возвращает частное от деления"""
  numerator = int(input("Введите делимое: "))
  denominator = int(input("Введите делитель: "))
  try:
    return numerator / denominator
  except ZeroDivisionError:
    return "На ноль делить нельзя"
