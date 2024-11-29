a = []
n = int(input('n='))

for i in range(1,n+1):
    a.append(i)
print(a[0])
i = 0
j = 0
k = 0
while k < n-1 :
    if a[i] != 0 :j += 1
    if j == 3 :
        a [i] = 0
        k += 1
        j = 0
    i += 1
    if i == n : i =0

for i in a:
    if i != 0 :
        print(i)
