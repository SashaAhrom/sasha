import random
import math
n=int(input("Введите размер списка n:\n"))
A=[]
B=[]
for i in range(n):
    a=random.randint(0,100)
    A.append(a)
x=0
y=math.ceil(n/2) # округление числа вверх
while x<y:       # создание половина списка
    B.append(A[x])
    x+=1
nmax=B.index(max(B)) # max индекс
nmin=B.index(min(B)) # min индекс

print("Список "+str(A)+"первая половина списка"+str(B))
print("max значение списка "+str(max(B)))
print('его индекс '+str(nmax))
print("min значение списка "+str(min(B)))
print('его индекс '+str(nmin))