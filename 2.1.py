a=int(input("Введите значение А "))
b=int(input("Введите значение B "))
A=[]
while a<=b:
    A.append(a*2)
    a+=1
A.reverse()
for i in range(len(A)):
    print(A[i])


