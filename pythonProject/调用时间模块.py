import time
print(time.time())
print(time.ctime())
print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime()))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime()))
