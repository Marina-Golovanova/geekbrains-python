from sys import argv

_, hours, rate_per_hour, premium = argv

print("Выработка в часах: ", hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", premium)
print(f'Заработная плата: {int(hours)*int(rate_per_hour)+int(premium)}')
