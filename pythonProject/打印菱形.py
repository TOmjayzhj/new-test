l = 1
k = 3
for i in range(0,4):
    for j in range(0,k):
        print(" ",end="")
    for j in range(0,l):
        print("*",sep=" ",end="")
    print()
    k-=1
    l+=2

l = 5
k = 1
for i in range(0,3):
    for j in range(0,k):
        print(" ",end="")
    for j in range(0,l):
        print("*",sep=" ",end="")
    print()
    k+=1
    l-=2

