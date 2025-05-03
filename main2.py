class BMW:
    def start_engine(self):
        return "BMW engine started."

    def drive(self):
        return "BMW is driving smoothly."

class Ferrari:
    def start_engine(self):
        return "Ferrari engine roars to life."

    def drive(self):
        return "Ferrari is speeding on the track."

# Polymorphism in action
def test_drive(car):
    print(car.start_engine())
    print(car.drive())

# Create instances of both classes
bmw_car = BMW()
ferrari_car = Ferrari()

# Test drive both cars
test_drive(bmw_car)
test_drive(ferrari_car)