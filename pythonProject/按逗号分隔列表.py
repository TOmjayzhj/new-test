'''
a = [1,2,3,4,5,6,7]
flag = 0
for i in a[0:7]:
    if flag == 0:
        print(i,end='')
        flag += 1
    else :
        print(",",end='')
        print(i,end='')
'''

l_str = "FracturedSheep"
l = list(l_str)
result = ",".join(l_str)
print(result)