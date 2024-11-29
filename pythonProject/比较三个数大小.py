num1 = int(input())
num2 = int(input())
num3 = int(input())
'''
a = []
a.append(num1)
a.append(num2)
a.append(num3)
a.sort()
print(a)
'''
t = 0
if num1 > num2 :
    t = num2
    num2 = num1
    num1 = t
if num1 > num3 :
    t = num1
    num1 = num3
    num3 = t
if num2 > num3 :
    t = num2
    num2 = num3
    num3 = t
print(num1,num2,num3)
