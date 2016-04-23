# Implement builder pattern using python .
# Assume we want to build a car , but we have many options .
# Car : wheels , color, seats, brand ,style etc.

# one way to produce a vehicle instance .

class Vehicle:
    # This is normal car with four wheels  .
    def __init__(self, wheels, color, seats, brand, style):
        self.wheels = wheels
        self.color = color
        self.seats = seats
        self.brand = brand
        self.style = style


    # But we want to produce a car without brand . how to do this ?
    # A possible way .
    def __init__(self, wheels, color, seats, style):
        self.wheels = wheels
        self.color = color
        self.seats = seats
        self.style = style

    # Ok, we do it .But someone want a moto without style and style  . How to dow this ?
    # definite another constructor .
    def __init__(self, wheels, color, seats):
        self.wheels = wheels
        self.color = color
        self.seats = seats

    # if we have too many requests ,we must define too many constructors .
    # so we have builder pattern .


class Vehicle_:

    def __init__(self):
        self.wheels = None
        self.color = None
        self.seats = None
        self.brand = None
        self.style = None


class BuildVehicle:
    def __init__(self):
        self.vehicle = Vehicle_()

    def set_wheels(self,wheels):
        self.vehicle.wheels = wheels

    def set_color(self, color):
        self.vehicle.color = color

    def set_seats(self, seats):
        self.vehicle.seats = seats

    def set_brand(self, brand):
        self.vehicle.brand = brand

    def set_style(self, style):
        self.vehicle.style = style

    def getVehicle(self):
        return self.vehicle


def main():
    # we want a car with color red .
    build_vehicle = BuildVehicle()
    build_vehicle.set_color("red")
    build_vehicle.set_brand("ModelX")
    build_vehicle.set_seats(4)
    build_vehicle.set_style("normal")
    build_vehicle.set_wheels(2) # two wheels , brand: ModelX, four sets normal style .

    vehicle = build_vehicle.getVehicle()

    print vehicle, vehicle.brand, vehicle.color, vehicle.wheels, vehicle.style, vehicle.seats


if __name__ == '__main__':
    main()