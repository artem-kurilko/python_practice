
class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is driving")


class Engine:
    def start(self):
        print("Engine start")


e = Car(Engine())
e.drive()
