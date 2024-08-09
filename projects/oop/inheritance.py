class Animal:
    def __init__(self, name, age, sound=None):
        self.name = name
        self.age = age
        self.sound = sound

    def show(self):
        print(f"I am {self.name} and I am {self.age} years olf. Also I say {self.sound}")

    def speak(self):
        if self.sound is not None and len(self.sound) > 0:
            print(self.sound)
        else:
            print("Donnow🫂")


class Dog(Animal):
    pass


x = Dog('John', 20)
print(x.__dict__)
# x.show()
# x.speak()
