revenue = int(input("Введите прибыль компании: "))
cost = int(input("Введите издержки компании: "))
if revenue > cost:
  rent = (revenue - cost) / revenue
  print(f"Фирма работает в прибыль. Рентабельность составляет {rent}")
  workers = int(input("Введите количество сотрудников: "))
  rent_worker = (revenue - cost) / workers
  print(f"Прибыль на сотрудника составляет %.2f руб." % rent_worker)
else:
  print("Компания работает в убыток.")
