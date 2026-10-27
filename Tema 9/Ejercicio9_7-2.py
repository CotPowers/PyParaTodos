nombre_archivo = input("Ingresa un nombre de archivo: ").strip()

dias_conteo = dict()

try:
    manejador = open(nombre_archivo)
    for linea in manejador:
        # Solo líneas de sobre que empiezan con "From " (ignora "From:")
        if not linea.startswith("From "):
            continue

        palabras = linea.split()

        # Guardián: asegura que existan al menos 3 elementos para evitar IndexError
        if len(palabras) < 3:
            continue

        # La tercera palabra es el día (índice 2)
        dia = palabras[2]

        # Acumulador con método .get()
        dias_conteo[dia] = dias_conteo.get(dia, 0) + 1

    manejador.close()
    print(dias_conteo)

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")