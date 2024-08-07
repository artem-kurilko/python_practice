n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input().strip()

total_val = 0
for x in student_marks[query_name]:
    total_val += x

res_val = total_val/len(student_marks[query_name])
formated_val = "{:.2f}".format(res_val)
print(formated_val)
