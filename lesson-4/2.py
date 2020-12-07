my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = (my_list[index+1] for index in range(len(my_list)-1) if my_list[index] < my_list[index+1])
print(list(new_list))
