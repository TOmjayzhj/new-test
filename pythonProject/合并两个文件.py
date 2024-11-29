fp1 = open("fire","r")
a = fp1.read()
print(a)
fp1.close()

fp2 = open("abcd","r")
b = fp2.read()
print(b)
fp2.close()

'''
fp3 = open("fire","w")
c = list(a+b)
c.sort()
s = ''
s = s.join(c)
fp3.write(s)
fp3.write("Holy shit")
print(b)
fp3.close()
'''
fp3 = open("Holy 2.0","r")
b = fp3.read()
print(b)
fp3.close()