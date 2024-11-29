
count = 0
for i in range(1,101):
    flag = 0
    if i == 2 :
        flag = 1
    for j in range(2,i):
       if i % j == 0:
            flag = 0
            break
       flag = 1

    if flag == 1:
        print(i,end='')
        print(" ",end='')
        count += 1
        if count % 5 == 0:
            print()
'''
a = int(input('a='))
b = int(input('b='))
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False

    return True

for i in range(a,b+1):
    if i >= 2 and isPrime(i):
        print(i)
'''