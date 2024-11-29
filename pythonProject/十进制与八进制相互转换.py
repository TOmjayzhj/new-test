'''
八进制转十进制
n = 0
p = input()
for i in range(len(p)):
    n = n*8 + int(p[i])
print(n)
'''


a = 12345
print(len(str(a)))
sum = 0
j = 0
for i in range(len(str(a))):
    j = a%10
    a //= 10
    print(j)
    sum += j*8**i
print(sum)