class Student:
    def __init__(self,id,name,math,english,chinese):
        self.id = id
        self.name = name
        self.math = math
        self.english = english
        self.chinese = chinese
        self.average = (math+english+chinese)/3

def sort_students(students):
    return sorted(students,key=lambda x:x.average,reverse=True)

n = int(input('n = '))
students = []
for i in range(n):
    id = input('id : ')
    name = input('name : ')
    math = float(input('math = '))
    english = float(input('english = '))
    chinese = float(input('chinese = '))
    students.append(Student(id,name,math,english,chinese))
sorted_students = sort_students(students)

print("id name average")
for student in sorted_students:
    print(f"id:{student.id}, name:{student.name}, average:{student.average}")