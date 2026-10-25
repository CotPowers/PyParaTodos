numeros = []

while True:
    entrada = input("Introduce un número: ")
    
    
    if entrada.strip().lower() == "hecho":
        break

    
    try:
        valor = float(entrada)
        numeros.append(valor)
    except ValueError:
        print("Entrada inválida")


if len(numeros) > 0:
    print(f"Máximo: {max(numeros)}")
    print(f"Mínimo: {min(numeros)}")
else:
    print("No se introdujo ningún número válido.")