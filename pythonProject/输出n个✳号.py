'''
n = 0
while n!=7 :
    a = int(input("a = "))
    if (a<=50 and a>0) :
        print(a*'*')
    n += 1
'''
for i in range(7):
    num = int(input('num = '))
    while not(num>=1 and num<=50):
        num = int(input('num = '))
    print(num*'*')