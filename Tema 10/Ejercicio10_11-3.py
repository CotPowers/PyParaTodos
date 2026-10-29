import string

nombre_archivo = input("Ingresa un nombre de archivo: ").strip()

conteo_letras = dict()
abecedario = string.ascii_lowercase

try:
    manejador = open(nombre_archivo)
    for linea in manejador:
        linea = linea.lower()
        for caracter in linea:
            if caracter in abecedario:
                conteo_letras[caracter] = conteo_letras.get(caracter, 0) + 1

    manejador.close()

    # Invertir pares a (frecuencia, letra) para ordenar por volumen
    lista_frecuencias = list()
    for letra, conteo in conteo_letras.items():
        lista_frecuencias.append((conteo, letra))

    lista_frecuencias.sort(reverse=True)

    for conteo, letra in lista_frecuencias:
        print(letra, conteo)

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")