import json
data = []
profit = {}
summa = 0
i = 0
with open("firms.txt") as f:
  sal = f.readlines()
  for line in sal:
    name, form, income, cost = line.split()
    profit.setdefault(name)
    profit[name] = int(income) - int(cost)
  for el in profit.keys():
    if profit.get(el) >= 0:
      summa += profit.get(el)
      i += 1
    average = summa / i
  new_dict = {"average": average}
  data.append(profit)
  data.append(new_dict)
print(data)

with open("firms.json", 'w') as f:
  json.dump(data, f)
