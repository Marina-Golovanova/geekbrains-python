class Clothes:
  materials = 0

  def __init__(self, name, weigth = 0, high = 0):
    self.name = name
    self.weigth = weigth
    self.high = high

  @staticmethod
  def get_square_all():
    return f'Общий размер ткани {Clothes.materials}'

class Coat(Clothes):
  def __init__(self, name, weigth):
    super().__init__(
      name=name,
      weigth=weigth
    )
    Clothes.materials += self.weigth / 6.5 + 0.3

  def get_square_coat(self):  
    return self.weigth / 6.5 + 0.3

  def __str__(self):
    return f'Размер ткани для пальто {self.get_square_coat()}'

class Costume(Clothes):
  def __init__(self, name, high):
    super().__init__(
      name=name,
      high=high
    )
    Clothes.materials += self.high * 2 + 0.3

  def get_square_costume(self):
    return self.high * 2 + 0.3

  def __str__(self):
    return f'Размер ткани для костюма {self.get_square_costume()}'

costume_1 = Costume('costume', 165)
coat_1 = Coat('coat', 3)

print(costume_1)
print(coat_1)
print(Clothes.get_square_all())
