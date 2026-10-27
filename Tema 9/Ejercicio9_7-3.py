nombre_archivo = input("Ingresa un nombre de archivo: ").strip()

remitentes = dict()

try:
    manejador = open(nombre_archivo)
    for linea in manejador:
        # Filtrar solo líneas que empiezan exactamente con "From "
        if not linea.startswith("From "):
            continue

        palabras = linea.split()

        # Guardián: verificar que la línea tenga al menos el remitente
        if len(palabras) < 2:
            continue

        # La segunda palabra es la dirección de correo
        correo = palabras[1]

        # Construir el histograma con .get()
        remitentes[correo] = remitentes.get(correo, 0) + 1

    manejador.close()
    print(remitentes)

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")