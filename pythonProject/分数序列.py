a = 1
b = 2
sum = 0
for i in range(0,20):
    sum += b/a
    c = a
    a = b
    b = c+b

print(sum)