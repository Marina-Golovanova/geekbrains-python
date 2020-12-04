summa = 0
while True:
  numbers = input().split(" ")
  has_stop = False
  for i in numbers:
    if i == "stop":
      has_stop = True
      break
    i = int(i)
    summa += i
  print(summa)
  if has_stop:
     break
