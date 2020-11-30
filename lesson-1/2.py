times = int(input("Введите время в секундах: "))
hour = times // 3600
minutes = (times - hour * 3600) // 60
sec = (times - hour * 3600) - (minutes * 60)
#print(hour, minutes, sec, sep=":")
print(f"{hour}:{minutes}:{sec}")