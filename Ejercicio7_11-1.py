nombre_archivo = input("Introduce el nombre del archivo: ")

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # .rstrip() elimina el salto de línea sobrante del archivo
            print(linea.rstrip().upper())

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")