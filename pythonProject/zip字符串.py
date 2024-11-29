a = input()
b = ""
c = a + '#'
i = 0
while c[i]!= '#':
    n = 1
    while c[i] == c[i+n]:
        n += 1
    if n > 1 :
        b = b  + str(n)+ a[i]
    else :
        b = b + a[i]
    i = i+n

print(b)
