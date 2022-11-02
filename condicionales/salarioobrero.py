from tkinter import E


a = input("ingrese horas trabajadas: ")
b = float(a)
c = b - 40
d = (40 * 2600) + (c * 5000)
e = b * 2600
if b > 40:
    print("su salario es: ", d)
elif b < 40:
    print("su salario es: ", e)
