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

