n = list(map(int, input("Введите число: ")))
i = 0
maximum = n[0]
while i < len(n):
  if n[i] >= maximum:
    maximum = n[i]
  i = i + 1
print(maximum)
