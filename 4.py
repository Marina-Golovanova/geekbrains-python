class Car():
  car_counter = 0
  inf_cars = {}
  is_drive = False

  def __init__(self, speed, color, name, is_police = False):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police
    Car.inf_cars[name] = [self.speed, self.color, self.is_police]
    Car.car_counter += 1

  def go(self):
    Car.is_drive = True
    return f'Автомобиль {self.name} поехал.'

  def stop(self):
    Car.is_drive = False
    return f'Автомобиль {self.name} остановился.'

  def turn(self, side):
    side = side.lower()
    if side == 'left' or side == 'лево' or side == 'налево' or side == 'влево':
      return f'Автомобиль {self.name} повернул налево.'
    elif side == 'rigth' or side == 'право' or side == 'направо' or side == 'вправо':
      return f'Автомобиль {self.name} повернул направо.'
    elif side == 'reversal' or side == 'разворот':
      return f'Автомобиль {self.name} развернулся.'
  
  

  def show_speed(self):
    if Car.is_drive == True:
      return f'Текущая скорость автомобиля {self.name} {self.speed} км/ч.'
    else:
      return f'Автомобиль {self.name} стоит'

  def __str__(self):
    return f'Автомобиль {self.name}. Автомобиль в движении: {Car.is_drive}. Полицейская: {self.is_police}'

class TownCar(Car):
  def __init__(self, speed, color, name, is_police = False):
    super().__init__(speed, color, name, is_police)

  def show_speed(self):
    if self.speed > 60:
      return f'Превышение скорости!'
    elif Car.is_drive == True:
      return f'Текущая скорость автомобиля {self.name} {self.speed} км/ч.'
    else:
      return f'Автомобиль стоит'


class SportCar(Car):
  def __init__(self, speed, color, name, is_police = False):
    super().__init__(speed, color, name, is_police)

class WorkCar(Car):
  def __init__(self, speed, color, name, is_police = False):
    super().__init__(speed, color, name, is_police)

  def show_speed(self):
    if self.speed > 40:
      return f'Текущая скорость автомобиля {self.name} {self.speed} км/ч. Превышение скорости!'
    elif Car.is_drive == True:
      return f'Текущая скорость автомобиля {self.name} {self.speed} км/ч.'
    else:
      return f'Автомобиль стоит'

class PoliceCar(Car):
  def __init__(self, speed, color, name, is_police = True):
    super().__init__(speed, color, name, is_police)

kia_rio = TownCar(60, 'white', 'Rio')
toyota = SportCar(200, 'green', 'Toyota')
renault_logan = WorkCar(50, 'black', 'Logan')
ford_focus = PoliceCar(60, 'grey', 'Focus')

print(kia_rio)
print(toyota.turn('left'))
print(renault_logan.show_speed())
print(ford_focus.go())
print(ford_focus.stop())
print(Car.inf_cars)
print(ford_focus.show_speed())
print(ford_focus.go())
print(ford_focus.show_speed())
print(f'Количество автомобилей в базе: {Car.car_counter}')
