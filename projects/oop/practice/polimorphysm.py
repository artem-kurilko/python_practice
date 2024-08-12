class Animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self):
        super().__init__('Bark')


class Cat(Animal):
    def __init__(self):
        super().__init__('Meow')


dog = Dog()
cat = Cat()
dog.make_sound() # "Bark"
cat.make_sound()  # "Meow"

