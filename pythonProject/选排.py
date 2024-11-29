a = []
n = int(input('n='))
for i in range(n):
    a.append(int(input('输入一个数')))

print(len(a))
'''
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1] :
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
'''

for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j] :
            t = a[i]
            a[i] = a[j]
            a[j] = t

for i in range(0,len(a)):
    print(a[i],end='')