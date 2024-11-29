num = input()
flag = 0
t = len(num)//2
for i in range (0,t):
    if num[i] == num [2*t-i]:
        flag += 1

if flag == t:
    print("这是一个回文")
else :
    print("这个不是哦")
