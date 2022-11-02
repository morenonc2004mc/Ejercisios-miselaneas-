num = []
print("Cuantos numeros desea ingresar")
n = int(input())
i=0
while i < n:
    print("Valor numero: ",i+1)
    val = float(input())
    num.append(val)
    i+=1
prom = sum(num) / len(num)
print("El promedio es: ",prom)

#suma de la lista

list = [1, 2, 3, 4, 5]
def sumar(list):
    suma = 0
    for elemento in list:
        suma += elemento
    return suma 
print(sumar(list))

