a = 4
sum = 0
n = int(input('n='))
for i in range(1,n+1):
    if i==2 :
        a = a*7
    elif i>2 :
        a = a*8
    sum += a
    print("{0}位数有{1}个".format(i,a))
    print(sum);
