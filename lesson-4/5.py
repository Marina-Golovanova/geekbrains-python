from functools import reduce

my_list = (el for el in range(99, 1001) if el % 2 == 0)

def multiplication(prev_el, el):
  return prev_el * el

print(reduce(multiplication, list(my_list)))
