class Human:
    def __init__(self, name="Human", gasoline = 10):
        self.name = name
        self.gasoline = gasoline

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passanger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passenger_name(self):
        if self.passengers != []:
            print(f"names of {self.brand} passengers: ")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"There are no passengers in {self.brand}")

andryi = Human("Andryi")
marko = Human("Marko")
alex = Human("Olexandr")

car = Auto("Mercedes")
car_2 = Auto("Tesla")

car.add_passanger(andryi, marko)
car_2.add_passanger(alex)

car.print_passenger_name()
car_2.print_passenger_name()