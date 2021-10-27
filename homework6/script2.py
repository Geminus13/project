class Road:
    _length = None
    _width = None

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculat(self):
         weight = 25
         thickness = 0.05
         result = (self._length * self._width * weight * thickness)/1000
         print(f'Потребуется {result} т')

my_road = Road(5000, 20)
my_road.calculat()
