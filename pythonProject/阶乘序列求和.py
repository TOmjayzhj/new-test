'''
sum = 0
for i in range(1,21):
    t = 1
    for j in range(1,i+1):
        t*=j
    sum+=t
print(sum)
##################################
def cheng(n):
    t = 1
    for i in range(1,n+1):
        t*=i
    return t

sum = 0
for i in range(1,21):
    sum+=cheng(i)

print(sum)
'''
def fact(n):
    if n==1 or n==0 :
        return 1
    else :
        return fact(n-1)*n

print(fact(5))