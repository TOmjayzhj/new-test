import time
start = time.time()
for i in range(10000):
    if i %1000 == 0 :print(i)
end = time.time()
print(end-start)

start = time.perf_counter()
for i in range(10000):
    if i % 1000 == 0:print(i)
end = time.perf_counter()
print(end-start)