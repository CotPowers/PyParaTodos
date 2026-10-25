cadena = 'X-DSPAM-Confidence:0.8475'

# 1. Encontrar la posición de los dos puntos
posicion_dos_puntos = cadena.find(':')

# 2. Extraer la porción después de los dos puntos usando slicing
porcion_extraida = cadena[posicion_dos_puntos + 1:]

# 3. Convertir a flotante
numero = float(porcion_extraida)

print(numero)
print(type(numero))  # Muestra: <class 'float'>