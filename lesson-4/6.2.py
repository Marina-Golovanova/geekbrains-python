from itertools import cycle
from sys import argv

_, text = argv

с = 0
for el in cycle(text):
    if с > 10:
        break
    print(el)
    с += 1
