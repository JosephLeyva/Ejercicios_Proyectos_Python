class Fan:
    def __init__(self, make: str, radius: float, color: str) -> None:
        self.make = make
        self.radius = radius
        self.color = color

        self.speed = 0
        self.isOn = False

    def switch_On(self):
        self.isOn = True
        self.speed = 3

    def switch_Off(self):
        self.isOn = False
        self.speed = 0

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        if (self.speed - how_much) > 0:
            self.speed -= how_much
        else:
            print("Get a Life")

    def __repr__(self) -> str:
        return repr((self.make, self.radius, self.color, self.speed, self.isOn))


fan = Fan("Manufacturer 1", 5, "Green")
fan.switch_On()
print(fan)

fan.switch_Off()
print(fan)

fan.switch_On()
fan.increase_speed(1)
print(fan)
