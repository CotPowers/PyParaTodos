nombre_archivo = input("Introduce el nombre del archivo: ")

total_spam = 0.0
contador = 0
prefijo = "X-DSPAM-Confidence:"

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # 1. Filtrar solo las líneas de interés
            if linea.startswith(prefijo):
                # 2. Localizar los dos puntos y rebanar el texto posterior
                posicion = linea.find(":")
                valor_texto = linea[posicion + 1:].strip()
                
                # 3. Convertir y acumular
                valor_flotante = float(valor_texto)
                total_spam += valor_flotante
                contador += 1

    # 4. Cálculo y muestra de resultados
    if contador > 0:
        media = total_spam / contador
        print(f"Líneas encontradas: {contador}")
        print(f"Total acumulado: {total_spam:.10f}")
        print(f"Media de spam confidence: {media:.10f}")
    else:
        print("No se encontraron líneas con el formato especificado en el archivo.")

except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")