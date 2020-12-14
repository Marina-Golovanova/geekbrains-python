from itertools import count
from sys import argv

_, first_number, last_number = argv

for el in count(int(first_number)):
    if el > int(last_number):
        break
    else:
        print(el)
