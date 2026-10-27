nombre_archivo = input("Ingresa un nombre de archivo: ").strip()

remitentes = dict()

try:
    manejador = open(nombre_archivo)
    for linea in manejador:
        if not linea.startswith("From "):
            continue

        palabras = linea.split()
        if len(palabras) < 2:
            continue

        correo = palabras[1]
        remitentes[correo] = remitentes.get(correo, 0) + 1

    manejador.close()

    # Patrón de bucle máximo (Capítulo 5)
    mayor_correo = None
    mayor_conteo = None

    for correo, conteo in remitentes.items():
        if mayor_conteo is None or conteo > mayor_conteo:
            mayor_conteo = conteo
            mayor_correo = correo

    print(mayor_correo, mayor_conteo)

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")