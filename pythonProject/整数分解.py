a = int(input("a="))
b = 1
while a>=9 :
    j = a % 10
    a = a//10
    b = b + 1
    print(j,end="")
print(a)
print(b)
