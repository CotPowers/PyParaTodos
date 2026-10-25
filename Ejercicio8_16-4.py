palabras_unicas = []

with open("romeo.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # 1. Separar la línea en una lista de palabras
            palabras = linea.split()
            
            # 2. Iterar palabra por palabra
            for palabra in palabras:
                # 3. Comprobar si no está en la lista para evitar duplicados
                if palabra not in palabras_unicas:
                    palabras_unicas.append(palabra)

    # 4. Ordenar alfabéticamente in-place
palabras_unicas.sort()

    # 5. Imprimir la lista resultante
print(palabras_unicas)

