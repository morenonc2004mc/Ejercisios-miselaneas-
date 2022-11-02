def ordenamiento_de_burbuja(lista):
    for n in range (len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp 

numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numeros)

ordenamiento_de_burbuja(numeros)
print(numeros)
