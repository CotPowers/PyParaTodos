
try:
    p = float(input('Escribe tu puntuacion: '))

    if p < 0.0 or p > 1.0:
        print("Puntuacion fuera de rango (debe ser entre 0.0 y 1.0)")
    elif p >= 0.9:
        print('Sobresaliente')
    elif p >= 0.8:
        print('Notable')
    elif p >= 0.7:
        print('Bien')
    elif p >= 0.6:
        print('Suficiente')
    else:
        print('Insuficiente')
except ValueError:
    print('Escribe una calificacion valida.')