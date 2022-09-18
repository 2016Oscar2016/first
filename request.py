class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"

class Smartphone(Display, Computer):
    def print_info(self):
        print(self.memory)
        print(self.resolution)
        print(self.model)

device = Smartphone(model = "Samsung")
device.print_info()