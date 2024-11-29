'''
ptr = [input("Please input the number :")for x in range(5)]
print(ptr)
ptr.reverse()
print(ptr)
for i in range(4,-1,-1):
    print(ptr[i])
'''
a = [3,4,5,1,4]
a.sort(reverse=True)
print(a)
a = a+[666]
print(a)
print(123+int('123'))