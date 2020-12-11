rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_list = []
with open("numbers.txt") as f:
  numb = f.readlines()
  for el in numb:
    el = el.split(" — ")
    el[0] = rus.get(el[0])
    new_list.append(el[0] + " - " + el[1])

with open("new_numbers.txt", 'w') as f_2:
  f_2.writelines(new_list)
