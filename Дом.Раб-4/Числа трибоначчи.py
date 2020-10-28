import time
def thb(n):
    x0 = 0
    x1 = 0
    x2 = 1
    print(0)
    print(0)
    for i in range(2,n):
        yield x2
        sum = x0 + x1 + x2
        x0 = x1
        x1 = x2
        x2 = sum


for x in thb(35):
    print(x)
    time.sleep(0.25)