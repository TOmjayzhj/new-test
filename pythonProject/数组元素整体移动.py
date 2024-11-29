'''
i = 0
j = 0
k = 0
while k < n-1 :
   if a[i] != 0 :j+=1
   if j == 3 :
      a[i] = 0
      k+=1
      j=0
   if i == n : i = 0
'''

a = [1,2,3,4,5,6,7,8]
b = [0,0,0,0,0,0,0,0]
m = int(input('m='))
t = 0
for m in range(m,len(a)):
    b[m] = a[t]
    t += 1
for i in range(len(b)-t):
    b[i] = a[t]
    t += 1

print(b)