nombre_archivo = input("Ingresa un nombre de archivo: ").strip()

horas_conteo = dict()

try:
    manejador = open(nombre_archivo)
    for linea in manejador:
        # Filtrar solo líneas que empiezan por "From "
        if not linea.startswith("From "):
            continue

        palabras = linea.split()

        # Guardián: verificar que la línea tenga al menos 6 palabras
        # From <email> <dia> <mes> <num_dia> <hora:min:seg> <año>
        #   0      1      2     3       4           5          6
        if len(palabras) < 6:
            continue

        # Extraer la cadena de tiempo (índice 5: "09:14:16")
        tiempo = palabras[5]

        # Dividir por el colon ":" para aislar la hora
        partes_tiempo = tiempo.split(":")
        hora = partes_tiempo[0]

        # Acumular la frecuencia de cada hora
        horas_conteo[hora] = horas_conteo.get(hora, 0) + 1

    manejador.close()

    # Ordenar por clave (hora) convirtiendo a lista de tuplas
    lista_horas = list(horas_conteo.items())
    lista_horas.sort()

    # Imprimir en el formato requerido: hora y cantidad
    for hora, conteo in lista_horas:
        print(hora, conteo)

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")