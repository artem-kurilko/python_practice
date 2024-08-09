# OOP core
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            if isinstance(student, Student):
                self.students.append(student)
                return True
        return False

    def get_average_grade(self):
        total_grade = 0
        for pupil in self.students:
            total_grade += pupil.get_grade()
        return total_grade/len(self.students)


s1 = Student('Tim', 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course('Python', 5)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(f'{course.get_average_grade():.2f}')