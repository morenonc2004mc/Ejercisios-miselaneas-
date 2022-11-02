numero_digitado= input("escribe un numero: ")
numero = float(numero_digitado)
if numero == 0:
    print("cero")
elif numero < 0:
    print("negativo")
else:
    print("positivo")
