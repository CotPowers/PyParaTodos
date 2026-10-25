nombre_archivo = input("Ingresa un nombre de archivo: ")

# Huevo de pascua
if nombre_archivo == "na na boo boo":
    print("NA NA BOO BOO PARA TI - Te he atrapado!")
    exit()

# Intentar abrir el archivo
try:
    man_a = open(nombre_archivo)
except:
    print("El archivo no puede ser abierto:", nombre_archivo)
    exit()

# Contar las líneas que empiezan con 'Subject:'
contador = 0
for linea in man_a:
    if linea.startswith("Subject:"):
        contador = contador + 1

print(f"Hay {contador} líneas subject en {nombre_archivo}")