diccionario_palabras = dict()

try:
    with open('words.txt', "r", encoding="utf-8") as manejador:
        for linea in manejador:
            # Dividir la línea en palabras individuales
            palabras = linea.split()
            for palabra in palabras:
                # Almacenar la palabra como clave (el valor no importa)
                diccionario_palabras[palabra] = None

    print(f"Se cargaron {len(diccionario_palabras)} palabras únicas en el diccionario.")

    # Comprobación interactiva con el operador in
    while True:
        busqueda = input("\nIngresa una palabra para buscar (o 'fin' para salir): ").strip()
        if busqueda.lower() == "fin":
            break
        
        if busqueda in diccionario_palabras:
            print(f"'{busqueda}' SÍ está en el diccionario.")
        else:
            print(f"'{busqueda}' NO se encuentra en el archivo.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo 'words.txt'. Revisa la ruta.")