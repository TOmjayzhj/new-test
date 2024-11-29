a = input('a = ')
a = a.split(" ",1)
offset = int(a[0])
aa = a[1]
str = ""

for i in aa :
    sn = ord(i)
    if i>='a' and i<='z':
        sn = (sn-97+ offset )%26+97
    elif i>='A' and i <='Z':
        sn = (sn-65+ offset)%26+65
    else :
        sn =sn
    str += chr(sn)

print(str)