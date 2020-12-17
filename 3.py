class Worker():
  _income_elements = {}
  workers_counter = 0

  def __init__(self, name, surname, position, wage, bonus):
    self.name = name
    self.surname = surname
    self.position = position
    self._income = {"wage": wage, "bonus": bonus}
    Worker.workers_counter += 1

class Position(Worker):
  def __init__(self, name, surname, position, wage, bonus):
    super().__init__(name, surname, position, wage, bonus)

  def get_full_name(self):
    return f'{self.name} {self.surname}'

  def get_total_income(self):
    total_income = self._income.get('wage') + self._income.get('bonus')
    return total_income

worker_1 = Position('Марина', 'Голованова', 'sociolog', 16000, 5000)
print(f'ФИО сотрудника: {Position.get_full_name(worker_1)}. Доход сотрудника: {Position.get_total_income(worker_1)}.')
