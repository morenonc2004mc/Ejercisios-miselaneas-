def fecha_dia_siguiente(año, mes, dia):
    bisiesto = False
    if año % 400 == 0:
        bisiesto = True
    elif año % 100 == 0:
        bisiesto = False 
    elif año % 4 == 0:
        bisiesto = True
    
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else: 
            dias_mes = 28
    else:
        dias_mes = 30
    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            año += 1
        else:
            mes = 1

    return (año, mes, dia)

print(fecha_dia_siguiente(2022, 6, 14))