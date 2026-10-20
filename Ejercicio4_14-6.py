def calculo_salario(horas, tarifa):
    """Calcula el salario aplicando tarifa y media (1.5x) a las horas > 40."""
    if horas > 40:
        horas_extra = horas - 40
        return (40 * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        return horas * tarifa


# Captura y validación de entradas
try:
    horas = float(input("Introduzca Horas: "))
    tarifa = float(input("Introduzca Tarifa: "))
except ValueError:
    print("Error, por favor introduzca un número")
    quit()  # Solo salimos si el usuario metió texto en vez de números

# Llamada a la función e impresión del resultado
salario = calculo_salario(horas, tarifa)
print(f"Salario: {salario}")