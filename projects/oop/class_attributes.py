class Person:
    __peoples = []
    num_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.num_of_people += 1
        Person.__peoples.append(self)

    @classmethod
    def get_people_num(cls):
        return cls.num_of_people

    @staticmethod
    def get_peoples():
        return Person.__peoples


p1 = Person('John')
p2 = Person('Mary')

for x in Person.get_peoples():
    print(x.__dict__)

