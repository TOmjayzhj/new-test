a = 10
b = 20
'''
c = a
a = b
b = c
'''
a,b=b,a
print(a,b)

'''
a = a + b
b = a - b
a = a - b

print(a,b)
'''
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)