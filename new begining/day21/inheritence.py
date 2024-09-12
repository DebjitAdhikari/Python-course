class Animal:
    def __init__(self):
        self.eyes=2
    def breathe(self):
        print("Inhale, exhale")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("under the water")

dog1=Dog()
print(dog1.eyes)
dog1.breathe()