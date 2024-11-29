a = []
n = int(input())
for i in range(0,n):
    a.append([])
    for j in range(n):
        a[i].append(float(input()))

sum = 0;
for i in range(n):
    sum += a[i][i]
    sum += a[i][n-1-i]

print(sum)