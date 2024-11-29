n = int(input('n = '))
a = n//1000
b = n//100%10
c = n//10%10
d = n%10
print(a,b,c,d)
sum = 0
a = (a+5)%10
b = (b+5)%10
c = (c+5)%10
d = (d+5)%10
sum = d*1000 + c*100 + b*10 +a
print(sum)