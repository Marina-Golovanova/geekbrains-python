class Road():
  road_counter = 0

  def __init__(self, length, width):
    self._length = length
    self._width = width
    Road.road_counter += 1
  
  def asphalt_mass_calculation(self, mass_for_one_square_metr, thickness):
    if type(mass_for_one_square_metr) != int or type(thickness) != int:
      raise TypeError("Введите числовые показатели!")

    asphalt_mass = self._length * self._width * mass_for_one_square_metr * thickness
    return f'Asphalt mass is {asphalt_mass/1000} tons'


A4 = Road(20, 5000)
print(A4.asphalt_mass_calculation(5, 25))
