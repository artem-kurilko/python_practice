class Flyable:
    def fly(self):
        print("Flying")


class Swimable:
    def swim(self):
        print("Swiming")


class Duck(Flyable, Swimable):
    pass


d = Duck()
d.swim()
d.fly()
