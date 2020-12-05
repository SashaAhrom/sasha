t1=int(input("Введите 1-ое число  "))
t2=int(input("Введите 2-ое число  "))
t3=int(input("Введите 3-е число  "))
t4=int(input("Введите 4-ое число  "))
t5=int(input("Введите 5-ое число  "))
A=[]
A.append(t1)
A.append(t2)
A.append(t3)
A.append(t4)
A.append(t5)
a=int(input("Введите индекс элемента в массиве "))
b=int(input("Введите число, на которое требуется увеличить элемент "))
print("Заданный массив   "+str(A))
tnew=A[a-1]+b
A.insert(a-1,tnew)
del A[a]
print("Измененный массив "+str(A))
