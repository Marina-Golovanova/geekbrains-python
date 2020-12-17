from time import sleep

def count_down(time):
  '''Обратный отсчет секунд'''
  for sec in range(time, 0, -1):
    print(sec, end='\r')
    sleep(1)


class TrafficLight():
  __color = ['red', 'yellow', 'green']

  def running(self):
    while True:
      i = 0
      while(i < 3):
        print(f'TrafficLight is {TrafficLight.__color[i]}')
        if i == 0:
          count_down(7)
        elif i == 1:
          count_down(5)
        elif i == 2:
          count_down(7)
        i += 1

trafficLight = TrafficLight()
print(trafficLight.running())
