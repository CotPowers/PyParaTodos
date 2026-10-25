nombre_archivo = input("Ingresa un nombre de archivo: ")

contador = 0

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if not linea.startswith("From "):
                continue

            palabras = linea.split()

            
            if len(palabras) < 2:
                continue

            
            print(palabras[1])
            contador += 1

    print(f"Hay {contador} lineas en el archivo con la palabra From al inicio")

except FileNotFoundError:
    print(f"El archivo no puede ser abierto: {nombre_archivo}")