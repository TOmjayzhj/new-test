n = int(input('n:'))
print("%d=" % n,end="")
k = 2
while n != 1 :
    while n % k == 0 :
        print (k,sep="",end="")
        n/=k
        if n != 1 :
            print("*",sep="",end="")
    k+=1