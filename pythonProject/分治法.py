def sort(a,m,n):
    if m == n :return a[m]
    k = (m+n)//2
    u = sort(a,m,k)
    v = sort(a,k+1,n)
    if u>v :return u
    elif v>u:return v

a = []
n = int(input('n = '))
m = 0
for i in range(n):
    b = int(input('b='))
    a.append(b)
n = n-1
print(sort(a,m,n))