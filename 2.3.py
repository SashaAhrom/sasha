t=0
for i in range(10):
    x=float(input("Точка №"+str(i+1)+" Введите значение х "))
    y = float(input("Точка №" + str(i+1) + " Введите значение y "))
    if -4<=x<=3 and -1<=y<=1:
        t+=1
print("Кол-во попаданий - "+str(t))
print("Кол-во промахов - "+str(10-t))