def esPrimo(l):
    primos = []
    for i in l:
        p = 0
        if i == 1:
          primos.append(i)
        else:
          for j in range(1,i+1):
            if i % j == 0:
              p += 1
          if p == 2:
            primos.append(i)
    return primos
 
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(esPrimo(lista))
 
#sumatoria de los valores
print('La suma de los valores de la lista es %d' %(sum(lista)))
 
#promedio de valores
print('El promedio es %.2f' %(sum(lista) / len(lista)))