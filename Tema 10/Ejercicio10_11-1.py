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

    # 1. Crear la lista de tuplas (contador, email) para ordenar por cantidad
    lista_tuplas = list()
    for correo, conteo in remitentes.items():
        lista_tuplas.append((conteo, correo))

    # 2. Ordenar en orden inverso (mayor a menor)
    lista_tuplas.sort(reverse=True)

    # 3. El primer elemento [0] tiene el mayor conteo
    conteo_max, correo_max = lista_tuplas[0]
    print(correo_max, conteo_max)

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")