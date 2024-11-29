import time
import random
ans = random.randint(1,100)
a = 0
start = time.time()
while a != ans :
    a = int(input('a = '))
    if a > ans :
        print("Too big")
    elif a < ans :
        print("Too small")
    else :
        print("That's good")

end = time.time()
b = end - start
print("You have spent  %d scoends" % b)
if b <= 10 :
    print("You are fuck talent ！")
elif b <= 20 :
    print("Just so so")
else :
    print("Are you stupid ！")