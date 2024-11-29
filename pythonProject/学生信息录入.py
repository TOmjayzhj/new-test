def input_stu():
    for i in range(n):
        name = input("请输入学生姓名:")
        Chinese = int(input("Chinese :"))
        Math = int(input("Math :"))
        English = int(input("English :"))
        stu.append([])
        stu[i].append(name)
        stu[i].append(Chinese)
        stu[i].append(Math)
        stu[i].append(English)
def output_stu():
    for i in stu:
        print("-------%s-------" % i[0])
        print("Chinese : %d" % i[1])
        print("Math : %d" % i[2])
        print("English : %d" % i[3])

n = int(input('n='))
stu = []
input_stu()
output_stu()