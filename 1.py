class Matrix:
  def __init__(self, lists):
    self.lists = lists

  def __str__(self):
    new_str = ''
    for el in self.lists:
      new_str = new_str + ' '.join(map(str, el)) + '\n'
    return new_str 

  
  def __add__(self, matrix_2):
    def sum_lists(a, b):
      new_list = []
      for i in range(max(len(a), len(b))):
        if i > len(a)-1:
          new_el = b[i]
        elif i > len(b)-1:
          new_el = a[i]
        else:
          new_el = a[i] + b[i]
        new_list.append(new_el)
      return new_list

    def sum_matrix(a, b):
      new_matrix = []
      for i in range(max(len(a), len(b))):
        if i > len(a) - 1:
          new_matrix.append(b[i])
        elif i > len(b) - 1:
          new_matrix.append(a[i])
        else:
          new_matrix.append(sum_lists(a[i], b[i]))
      return new_matrix
    
    new_matrix = sum_matrix(self.lists, matrix_2.lists)
    return Matrix(new_matrix)

      


m_1 = Matrix([[1,2, 3], [2,3, 3], [4,9, 3]])
m_2 = Matrix([[2,3], [4,5], [8,9], [8,9]])
m_3 = m_1 + m_2
print(m_3)
