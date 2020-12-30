sal = []
poor_workers = []
with open("workers.txt", 'r') as f:
  my_list = f.read().split('\n')
  for el in my_list:
    el = el.split()
    if int(el[1]) < 20000:
      poor_workers.append(el[0])
    sal.append(int(el[1]))
print(f"Сотрудники с окладом менее 20000 руб.: {poor_workers}. \nСредний доход сотрудников: {sum(map(int, sal))/len(sal)}")
