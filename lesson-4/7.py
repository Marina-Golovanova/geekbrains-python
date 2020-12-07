def fact(n):
  res = 1
  for i in range(1, n + 1):
    res = res * i
    yield res

print(list(fact(4)))
