import requests
import os

while True:

    ciudad = input("De que lugar desea saber el clima?: (exit para salir) ")
    if ciudad.lower() == "exit":
        print("Vuelva pronto!")
        break 
    else:
        API_KEY= "1daf3e3e56d73310e7caa3137bf79d79"
        URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&lang=es&units=metric"

        respuesta = requests.get(URL)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            temperatura = datos['main']['temp']
            descripcion = datos['weather'][0]['description']
            os.system("cls")
            print(f"El clima en {ciudad} es: {descripcion} con una temperatura de {temperatura}°C")
        else:
            os.system("cls")
            print(f"Error al obtener los datos del clima, codigo {respuesta.status_code}")