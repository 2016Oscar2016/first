class Animals:
    def __init__(self, region, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs = "4 legs"
        self.region = region


class Gorilla(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_g = 2
        self.height_g = " from 1m to 2m"
        self.age_g = " from 30 to 50 years"

    def print_info(self):
        print(f"Gorilla legs:{self.legs_g}")
        print(f"Height:{self.height_g}")
        print(f"Age:{self.age_g}")
        print(f"Region:{self.region}\n")


class Mamont(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_m = 4
        self.height_m = " from 3m to 6m"
        self.age_m = " from 30 to 80 years"

    def print_info(self):
        print(f"Mamont legs:{self.legs_m}")
        print(f"Height:{self.height_m}")
        print(f"Age:{self.age_m}")
        print(f"Region:{self.region}\n")

class SeaHorse(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.legs_s = 0
        self.height_s =" from 1.5cm to 35.5cm"
        self.age_s = " from 4 to 5 years"

    def print_info(self):
        print(f"SeaHorse legs:{self.legs_s}")
        print(f"Height:{self.height_s}")
        print(f"Age:{self.age_s}")
        print(f"Region:{self.region}\n")


animal_m = Mamont(region="Ice")
animal_g = Gorilla(region="Africa")
animal_s = SeaHorse(region="Ocean")

animal_m.print_info()
animal_g.print_info()
animal_s.print_info()