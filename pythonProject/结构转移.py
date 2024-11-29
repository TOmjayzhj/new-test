class student:
    x = 0
    c = 0
def f(stu):
    stu.x = 20
    stu.c = 'c'
a = student()
a.x = 10
a.c = 'f'
print(a.x,a.c)
f(a)
print(a.x,a.c)