for i in range (2,1001):
    a = []
    total = 0
    for j in range (1,i) :
        if i % j == 0 :
            a.append(j)
            total += j
    if total == i :
        print(i)
        for j in a :
            print(j,' ',end='')
        print()


