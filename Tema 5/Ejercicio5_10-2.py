max = None
min = None

while True:
    num = input('Introduce numeros: ')
    if num == 'fin':
        break
    try:
        numero = float (num)
        if max is None or numero > max:
             max = numero
        if min is None or numero < min:
             min = numero
    except ValueError:
            print("Error: Introducir solo numeros o fin")
            continue

if max is not None and min is not None:
     print(f'Numero maximo: {max}')
     print(f'Numero minimo: {min}')
else:
    print('No se introdujeron numeros')
