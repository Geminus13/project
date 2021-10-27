class Cars:

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина поехала, скорость: {self.speed} км/ч'

    def stop(self):
        self.speed = 0
        return f'Машина остановилась, скорость: {self.speed} км/ч'

    def turn(self, direction):
        return f'Машина повернула: {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed} км/ч'

class TownCar(Cars):
    max_speed = 60

    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def show_speed(self):
        super().show_speed()
        if self.speed > self.max_speed:
            return 'Превышена скорость!'

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    max_speed = 40

    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def show_speed(self):
        super().show_speed()
        if self.speed > self.max_speed:
            return 'Превышена скорость!'

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

avto = TownCar('Ford', 70, 'белый')
print(avto.name, avto.color, avto.speed, avto.is_police)
print(avto.go())
print(avto.show_speed())
print(avto.turn('направо'))
print(avto.stop())

avto2 = WorkCar('BMW', 50, 'черный')
print(avto2.name, avto2.color, avto2.speed, avto2.is_police)
print(avto2.go())
print(avto2.show_speed())
print(avto2.turn('налево'))
print(avto2.stop())

avto3 = SportCar('Запорожец', 60, 'синий')
print(avto3.name, avto3.color, avto3.speed, avto3.is_police)
print(avto3.go())
print(avto3.show_speed())
print(avto3.turn('налево'))
print(avto3.stop())
