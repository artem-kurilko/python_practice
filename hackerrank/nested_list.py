# Live input
# num = int(input())
#
# my_list = []
# for _ in range(num):
#     name = str(input())
#     score = float(input())
#     my_list.append([name, score])


# my_list = [["Harsh", 20], ["Beria", 20], ["Varun", 19], ["Kakunami", 19], ["Vikas", 21]]
my_list = [["Prashant", 32], ["Pallavi", 36], ["Dheeraj", 39], ["Shivam", 40]]
sorted_list = sorted(my_list, key=lambda x: x[1], reverse=False)

grades = set()
for i in sorted_list:
    grades.add(i[1])

lowest_grade = sorted(grades)[1]
print("Lowest grade", lowest_grade)

bad_grades_students = []
for i in sorted_list:
    if i[1] == lowest_grade:
        bad_grades_students.append(i)

print("Bad grades students", bad_grades_students)

for i in sorted(bad_grades_students, key=lambda x: x[0]):
    print(i[0])
