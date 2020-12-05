import math

x=float(input("Введите значение х "))
n=int(input("Введите значение N "))
S=0
i=0
for i in range(n+1):
    S+=(((-1)**i)*(x**(i)))/math.factorial(i)
'''while i<=n:
    S += (((-1) ** i) * (x ** (i))) / math.factorial(i)
    i+=1'''
print("При Х="+str(x)+" и N="+str(n)+"  Сумма="+str(round(S,3)))