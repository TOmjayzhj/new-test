n = int(input())
a = n>>4
b = ~(~0<<4)
c = a&b
print("%o %o"%(n,c))
