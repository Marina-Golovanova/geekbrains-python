class Stationery():
  stationery_counter = 0

  def __init__(self, title):
    self.title = title
    Stationery.stationery_counter += 1

  def draw(self):
    return f'Запуск отрисовки.'
  
  def __str__(self):
    return f'Канцелярская принадлежность {self.title}'

class Pen(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return f'Запуск отрисовки ручкой.'

class Pencil(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return f'Запуск отрисовки карандашом.'

class Handle(Stationery):
  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    return f'Запуск отрисовки маркером.'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
print(handle)
print(f'Количество канцелярских предметов в базе: {Stationery.stationery_counter}')
