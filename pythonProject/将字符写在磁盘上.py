filename  = input()
fp = open(filename,"w")
s = input('输入字符串 ：')
while s!='#':
    fp.write(s+'\n')
    s = input('输入字符串 ：')
print("end")