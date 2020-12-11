with open("numbers.txt", 'w') as f:
  line = input("Введите числа: ").split()
  f.write(str(line))
  print(f"Сумма чисел: {sum(map(int, line))}")
  print(f"\nСумма чисел: {sum(map(int, line))}", file = f)
