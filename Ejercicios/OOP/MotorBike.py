class MotorBike:

    def __init__(self, speed) -> None:
        self.speed = speed

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self, how_much):
        if (self.speed - how_much) > 0:
            self.speed -= how_much
        else:
            print("Get a Life")


honda = MotorBike(50)
ducati = MotorBike(250)


honda.increase_speed(150)
ducati.increase_speed(25)


honda.decrease_speed(50)
ducati.decrease_speed(25)

print(honda.speed)
print(ducati.speed)
