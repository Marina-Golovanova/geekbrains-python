class Cell:
  count_cells = 0

  def __init__(self, size):
    self.size = size
    Cell.count_cells += self.size

  def __add__(self, other_cell):
    return f'Результат сложения двух клеток: {self.size + other_cell.size}'

  def __sub__(self, other_cell):
    if self.size - other_cell.size > 0:
      return f'Результат вычитания двух клеток: {self.size - other_cell.size}'
    else:
      return f'Разность количества ячеек двух клеток меньше нуля'

  def __mul__(self, other_cell):
    return f'Результат умножения двух клеток: {self.size * other_cell.size}'

  def __truediv__(self, other_cell):
    try:
      return f'Результат деления двух клеток: {round(self.size / other_cell.size)}'
    except ZeroDivisionError:
      return f'Операция невозможна'

  def make_order(self, cells_in_row):
    full_row = self.size // cells_in_row
    s = ""
    for i in range(full_row):
      s += '*' * cells_in_row + '\n'
    s += '*' * (self.size - full_row*cells_in_row)
    return s
    # while i > 0:
    #   row = i - cells_in_row
    #   s += row * "*"
    
cell_1 = Cell(8)
cell_2 = Cell(4)
print(cell_1+cell_2)
print(cell_2-cell_1)
print(cell_2*cell_1)
print(cell_1/cell_2)
print(cell_1.make_order(5))
