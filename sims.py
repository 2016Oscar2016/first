import random
cube = 0
dayr = 1

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
            self.car.strength -= 10
        else:
            self.repair()
            return
        self.job = Job()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 3

    def work(self):
        if self.car.drive():
            self.car.strength -= 10
        else:
            if self.car.fuel < 20:
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
            self.car.strength -= 10
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.repair()
                return
        if manage == "fuel":
            print("Fuel bought")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Food bought")
            self.money -= 25
            self.home.food += 50
        elif manage == "dedicates":
            print("YooHoo!! DELICIOUS!!!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 75

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
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:=^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food = {self.home.food}")
        print(f"Mess = {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:=^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Dead inside")
        if self.satiety < 0:
            print(" R.I.P")
        if self.money <= 50:
            print("Bankrot")
            return

    def live(self):
        cube == random.randint(1, 4)

        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled down in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car! {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job. I must get a job! {self.job.job} With salary: {self.job.salary}")
        if self.satiety < 20:
            print("Im gonna eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I wanna chill, but there is so much mess \n So I will clean the house")
                self.clean()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 100:
            print("Start working...")
            self.work()
        elif self.home.food <= 0:
            print("I'm very hungry!!!")
            self.shopping("food")
        elif self.car.strength < 100:
            print("I need to repair my car")
            self.repair()
        elif cube == 1:
            print("Let's chill!")
            self.chill()
        elif cube == 2:
            print("Statrt working...")
            self.work()
        elif cube == 3:
            print("Cleaning time!")
            self.clean()
        elif cube == 4:
            print("Time for shopping!!!")
            self.shopping()

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.strength = brand_list[self.brand]["strength"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
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

andriy = Human("Andriy")

for day in range(1001):
        andriy.live()
        andriy.is_alive()
        andriy.days(day)
