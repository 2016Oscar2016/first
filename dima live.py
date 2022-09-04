import random

class Student:

    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def study(self):
        print("studying")
        self.progress += 0.05
        self.happiness -= 7

    def sleep(self):
        print("sleeping")
        self.happiness +=3

    def chill(self):
        print("chill")
        self.happiness += 5
        self.progress -= 0.01
        self.money -=2

    def working(self):
        print("working")
        self.money +=6

    def is_alive(self):
        if self.progress < -0.05:
            print("BAN")
            self.alive = False
        elif self.progress > 5:
            print("ЗДАВ!")
            self.alive = False
        elif self.happiness <= 0:
            print("DEAD INSIDE")
            self.alive = False
        elif self.money > 500:
            print("Багатий! І школа не потрібна!")
            self.alive = False

    def end(self):
        print(f"Щастя: {self.happiness}")
        print(f"Успішність: {round(self.progress,2)}")
        print(f"Гроші: {self.money}")

    def live(self, day):
        day = "день " + str(day) + " " + self.name + " життя"
        print(f"{day:=^25}")
        random_cube = random.randint(1, 4)
        if random_cube == 1:
            self.study()
        elif random_cube == 2:
            self.sleep()
        elif random_cube == 3:
            self.chill()
        elif random_cube == 4:
            self.working()
        self.end()
        self.is_alive()

dima = Student(name="dima")

for day in range(1000):
    if dima.alive == False:
        break
    dima.live(day)