"""
Проект: Программа, которая считывает текст из файла и записывает изменённый текст в другой файл.
"""

lines = []


with open('file.txt', 'w') as file:
    file.write("Shit\n")
    file.write("ANOTHER shit\n")
    file.write("and oh yeah flowers\n")


with open('file.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        line += ' ADDED BONUS\n'
        lines.append(line)

with open('newfile.txt', 'w') as file:
    for line in lines:
        file.write(line)


print('Finish my hard work')