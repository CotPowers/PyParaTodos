manejador = open('mbox-short.txt')

for linea in manejador:
    palabras = linea.split()
    
    # Patrón guardián reforzado:
    # Si la lista tiene menos de 3 palabras, no puede contener palabras[2]
    if len(palabras) < 3 or palabras[0] != 'From':
        continue

    print(palabras[2])