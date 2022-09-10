import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping()
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
        self.satiety +5
        self.home.food -=3

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <20:
                self.shopping("fuel")
                return
            else:
                self.repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <20:
                self.shopping("fuel")
                return
            else:
                self.repair()
                return
        if manage == "fuel":
            print("Fuel bought")
            self.money -=100
            self.car.fuel += 100
        elif manage == "food":
            print("Food bought")
            self.money -=25
            self.home.food += 50
        elif manage == "dedicates":
            print("YooHoo!! DELICIOUS!!!")
            self.gladness += 10
            self.satiety += 2
            self.money -=75

    def chill(self):
        self.gladness += 10
        self.home.mess = 0
        self.money -= 10

    def clean(self):
        self.gladness -= 5
        self.home.mess = 0

    def repair(self):
        self.car.strength += 100
        self.money -= 50

    def bathroom(self):
        self.gladness += 10

    def days(self, day):
        day = f"today the {day} of {self.name}'s life"
        print(f"{day: =^10}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:=^50}", "\n")
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Gladness: {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food: {self.home.food}")
        print(f"Mess: {self.home.mess}")
        car_indexes = f"{self.car.brand}'s car indexes"
        print(f"{car_indexes:=^50}", "\n")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Dead inside")
        if self.satiety < 0:
            print(" R.I.P")
        if self.money <= 100:
            print("Bankrot")
            return

    def live(self):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.strength = brand_list[self.brand]["strength"]

    def drive(self):
        if self.horse_power > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.consumption -= 1
            return True
        else:
            print("The car can't move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    "It developer": {"salary": 100, "gladness_less": 15},
    "Car driver": {"salary": 50, "gladness_less": 10},
    "Fireman": {"salary": 100, "gladness_less": 25},
    "Doctor": {"salary": 25, "gladness_less": 5}
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Mercedes": {"fuel": 100, "strength": 150, "consumption": 8},
    "Tesla": {"fuel": 100, "strength": 175, "consumption": 5},
    "Ferrari": {"fuel": 80, "strength": 200, "consumption": 10}
}

class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]