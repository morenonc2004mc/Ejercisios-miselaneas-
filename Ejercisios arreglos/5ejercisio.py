n = int(input("Ingrese cuantos numeros desea agregar a la lista"))
list = []
for i in range(n):
    num = int(input("Ingrese numero {}: ".format(i+1)))
    list.append(num)
print(list)

num_enc = int(input("Ingrese el numero que quiere encontrar en la lista: "))
for j in range(len(list)):
    if num_enc == list[j]:
        print("El numero {} se ha encontrado en la posicion {}".format(num_enc,j))
    else:
        print("El numero {} no se ha encontrado en la posicion {}".format(num_enc,j))
