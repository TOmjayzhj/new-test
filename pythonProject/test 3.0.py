class Student():
    def __init__(self,id,num,math,english,computer):
        self.id = id
        self.name = name
        self.math = math
        self.english = english
        self.computer = computer
        self.average = (math + english + computer)/3

n = int(input('n = '))
students = []
for i in range(n):
    id = int(input('id = '))
    name = input('name = ')
    math = float(input('math = '))
    english = float(input('english = '))
    computer = float(input('computer = '))
    students.append(Student (id,name,math,english,computer))

sorted_students = sorted(students,key=lambda x:x.average ,reverse=True)

print("id  name  average")
for student in sorted_students:
    print(f"id :{student.id}, name :{student.name}, average :%.2f" % student.average)