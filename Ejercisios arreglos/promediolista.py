num = []
print("Cuantos numeros desea Ingresar")
n = int(input())
i=0
while i < n:
    print("Valor numero: ",i+1)
    val = float(input())
    num.append(val)
    i+=1
prom = sum(num) / len(num)
print("El promedio es: ",prom)