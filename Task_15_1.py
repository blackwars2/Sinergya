class Transport(object):
    name = "Ikarus"
    max_speed = 120
    mileage = 40


    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def auto(self):
        print(f"{self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

Autobus = Transport("Renault Logan", 180, 12)

Autobus.auto()
