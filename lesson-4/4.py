my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = (el for index, el in enumerate(my_list) if my_list.count(el) < 2)
print(list(new_list))
