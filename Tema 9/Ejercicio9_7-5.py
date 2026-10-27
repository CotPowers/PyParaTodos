nombre_archivo = input("Ingresa un nombre de archivo: ").strip()

dominios = dict()

try:
    manejador = open(nombre_archivo)
    for linea in manejador:
        # Filtrar solo líneas que empiezan exactamente con "From "
        if not linea.startswith("From "):
            continue

        palabras = linea.split()
        if len(palabras) < 2:
            continue

        # palabras[1] contiene el correo (ej: 'stephen.marquard@uct.ac.za')
        correo = palabras[1]

        # Dividir el correo por la arroba para extraer el dominio
        partes_correo = correo.split("@")
        if len(partes_correo) < 2:
            continue

        dominio = partes_correo[1]

        # Acumular conteo en el diccionario
        dominios[dominio] = dominios.get(dominio, 0) + 1

    manejador.close()
    print(dominios)

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")