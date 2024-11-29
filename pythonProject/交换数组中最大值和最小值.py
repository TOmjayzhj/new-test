a = []
n = int(input("n = "))
for i in range(n):
    num = int(input('num = '))
    a.append(num)

max = a[0]
min = a[0]
max_index = 0
min_index = 0
for i in range(n):
    if a[i] < min :
        min = a[i]
        min_index = i
temp = a[min_index]
a[min_index] = a[n-1]
a[n-1] = temp

for i in range (n):
    if a[i] > max :
        max = a[i]
        max_index = i
temp = a[max_index]
a[max_index] = a[0]
a[0] = temp

for i in a : print(i)