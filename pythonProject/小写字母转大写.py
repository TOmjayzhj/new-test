filename = input("filname:")
str = input("str = ")
str = str.upper()
print(str)
fp = open(filename,"w")
fp.write(str)
print("写入完毕")
fp = open(filename,"r")
print(fp.read())
print(str.lower())
