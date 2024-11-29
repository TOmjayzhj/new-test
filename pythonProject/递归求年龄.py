'''
def age(n):
    if n == 1:
        return 10
    return age(n-1)+2

print(age(5))
'''

age = [10]
n = int(input())
for i in range (0,n):
    age.append(age[i]+2)

print(age[n-1])