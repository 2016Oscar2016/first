class Animals:
    def __init__(self, region, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.region = region


class Mammals(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_a = "Mammals"

class Mamonts(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_d = "Mamont"

class Birds(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_b = "Birds"

class Fish(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_c = "Fish"


class Gorilla(Mammals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_g = 2
        self.height_g = " from 1m to 2m"
        self.age_g = " from 30 to 50 years"

    def print_info(self):
        print("Gorilla class:")
        print(f"Class: {self.class_a}")
        print(f"Region: {self.region}\n")
        print("Gorilla statistic:")
        print(f"Gorilla legs: {self.legs_g}")
        print(f"Height: {self.height_g}")
        print(f"Age: {self.age_g}\n")

class Mamont(Mamonts):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_m = 4
        self.height_m = " from 3m to 6m"
        self.age_m = " from 30 to 80 years"

    def print_info(self):
        print("Mamont class:")
        print(f"Class: {self.class_d}")
        print(f"Region: {self.region}\n")
        print(f"Mamont legs:{self.legs_m}")
        print(f"Height:{self.height_m}")
        print(f"Age:{self.age_m}")


class Sparrow(Birds):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wings_s = 2
        self.height_s = " from 15cm to 17cm"
        self.age_s = " from 2 to 4 years"

    def print_info(self):
        print("Sparrow class:")
        print(f"Class: {self.class_b}")
        print(f"Region: {self.region}\n")
        print(f"Sparrow wings:{self.wings_s}")
        print(f"Height:{self.height_s}")
        print(f"Age:{self.age_s}")

class Сrucian(Fish):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fins_f = 3
        self.height_f = "from 30cm to 50сm"
        self.age_f = "from 10 to 15 years"

    def print_info(self):
        print("Сrucian class:")
        print(f"Class: {self.class_c}")
        print(f"Region: {self.region}\n")
        print(f"Сrucian fins: {self.fins_f}")
        print(f"Height: {self.height_f}")
        print(f"Age: {self.age_f}")

animal_m = Mamont(region="Ice")
animal_g = Gorilla(region="Africa")
animal_s = Sparrow(region="Air")
animal_f = Сrucian(region="Water")

animal_g.print_info()
animal_m.print_info()
animal_s.print_info()
animal_f.print_info()