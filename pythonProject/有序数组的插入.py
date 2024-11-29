a = [1,5,9,11,21,0]
n = int(input('n='))
index = 0
##插入元素-----------

if n >= a[4]:
    a[5] = n
else:

    for i in range(0,5):
        if a[i] >= n :
            index = i
            break

    for i in range(4,index-1,-1):
        a[i+1] = a[i]

    a [index] = n


##for i in range(0,6):
##    print(a[i])

print(a)

##删除元素--------------
m = int(input('m='))
flag=0
for i in range(0,6):
    if m == a[i]:
        index = i
        flag = 1

if flag==0 :
    print("Not Found")
else:
    a[index] = a[index+1]
    for i in range(index,5):
        a[i] = a[i+1]

a[5]=0
print(a)

