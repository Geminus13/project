class Road:
    __length = None
    __width = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculat(self):
         weight = 25
         thickness = 0.05
         result = (self.__length * self.__width * weight * thickness)/1000
         print(f'Потребуется {result} т')

my_road = Road(5000, 20)
my_road.calculat()
