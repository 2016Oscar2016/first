class iter:
    def __init__(self, list = 16):
        self.list = list

    def __iter__(self):
        return self

    def __next__(self):
        self.list -= 1
        if not self.list:
            raise StopIteration()
        return self.list

iterator = iter()
for value in iterator:
    print(value)