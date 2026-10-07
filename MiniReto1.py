#Mini-reto: script que pida una hora y diga si el Proxmox debería estar encendido o apagado según tu horario


try:
    Hora = float(input('Que hora es? '))

    if 7.00 <= Hora <= 20.00:
        print('Proxmox encendido')
    else:
        print('Proxmox apagado')
except ValueError:
    print('Introducir hora valida')

#Corregido por Gemini

try:
    hora = float(input("¿Qué hora es? (formato 0-24, ej: 14.30): "))

    # Validación de rango de un día real
    if not (0.0 <= hora <= 24.0):
        print("Esa hora no existe en este planeta.")
    elif 7.0 <= hora <= 20.0:  # Equivale a: hora >= 7.0 and hora <= 20.0
        print("Proxmox encendido")
    else:
        print("Proxmox apagado")

except ValueError:
    print("Introduce un número válido.")