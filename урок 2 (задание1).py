'''Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b на квадраты
с наибольшей возможной на каждом этапе стороной. Выведите длины ребер получаемых квадратов
и кол-во полученных квадратов.'''

a=int(input("Введите сторану а:"))
b=int(input("Введите сторану b:"))

def del_pr(a,b):
    global kol_sc
    kol_sc = max(a, b) // min(a, b)
    print("Кол-во квадратов-" + str(kol_sc) + " шт. сторона у квадрата =" + str(min(a, b)))


while min(a, b)>0:
    del_pr(a,b)
    a=max(a, b)-(min(a, b)*int(kol_sc))
    b=max(a, b)

else:
    quit()