a = [1,2,3,4,5]
print((len(a)-1)//2)
for i in range(0,(len(a)-1)//2+1):
    temp = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = temp
print(a)
