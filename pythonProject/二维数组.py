'''
a = []
for i in range(3):
    b = []
    for j in range(3):
        c = int(input())
        b.append(c)
    a.append(b)
for i in a:print(i)
'''

a = []
n = int(input())
for i in range(n):
    a.append([])
    for j in range(i+1):
        if j == 0 or j==i :
            a[i].append(1)
        else:
            a[i].append(a[i-1][j]+a[i-1][j-1])
for i in a:print(i)
