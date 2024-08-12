
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is {} and I am {} years old".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print("Hello, my name is {} and I am {} years old. My grade is {}".format(self.name, self.age, self.grade))


student = Student("Alice", 20, "A")
student.introduce()