'''
import datetime

a = datetime()

str1 = "ABCDDDEFG&"
str2 = "DDD"
print(str1.count(str2))
print(str1.count('E'))
print(str1.count("D"))
print(str2.count('DD'))
'''
list = [1,2,3,3,3,4]
tuple1 = (1,2,3,3,3,4,4,5,5)
print(list.count(3))
print(tuple1.count(3))