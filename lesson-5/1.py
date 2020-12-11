with open("text.txt", 'x') as f:
  line = input("Введите строку: \n")
  while line != " ":
    f.writelines(line)
    line = input("Введите строку: \n")
