import requests

url = 'http://data.pr4e.org/romeo.txt'
respuesta = requests.get(url)

print("Estado de la conexión:", respuesta.status_code)
print("Contenido:\n", respuesta.text)