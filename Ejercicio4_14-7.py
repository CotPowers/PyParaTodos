def calcula_calificacion(p):

    if p < 0.0 or p > 1.0:
        return("Puntuacion fuera de rango (debe ser entre 0.0 y 1.0)")
    elif p >= 0.9:
        return('Sobresaliente')
    elif p >= 0.8:
        return('Notable')
    elif p >= 0.7:
        return('Bien')
    elif p >= 0.6:
        return('Suficiente')
    else:
        return('Insuficiente')

try:
    puntos = float(input('Escribe tu puntuacion: '))
except ValueError:
    print('Escribe una calificacion valida.')
    quit()  # Solo salimos si el usuario metió texto en vez de números

calificacion = calcula_calificacion(puntos)
print(f"Tu puntuacion es: {calificacion}")