import random

class Human:
    def __init__(self, name = "Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean(self):
        pass

    def repair(self):
        pass

    def bathroom(self):
        pass

    def days(self):
        pass

    def is_alive(self):
        pass

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
    "It developer": {"salary":100, "gladness_less": 15},
    "Car driver": {"salary":50, "gladness_less": 10},
    "Fireman": {"salary":100, "gladness_less": 25},
    "Doctor": {"salary":25, "gladness_less": 5}
}

brands_of_car = {
    "BMW":{"fuel":100,"strength":100, "consumption":6},
    "Mercedes":{"fuel":100,"strength":150, "consumption":8},
    "Tesla":{"fuel":100,"strength":175, "consumption":5},
    "Ferrari":{"fuel":80,"strength":200, "consumption":10}
}

class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]