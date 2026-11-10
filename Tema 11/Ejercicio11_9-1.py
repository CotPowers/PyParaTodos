import re

x = input('Introduce expresión regular: ')

contador = 0
try:

    manejador = open ('mbox.txt')

    for linea in manejador:

        if re.search (x, linea):
        
            contador = contador + 1

    print(f'El numero de lineas que coinciden es: {contador}')

except FileNotFoundError:
    print('El archivo no puede ser abierto: mbox.txt')