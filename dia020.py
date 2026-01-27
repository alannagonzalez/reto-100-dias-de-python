#TEMPORIZADOR DE EVENTOS:

import time
from datetime import datetime
from datetime import timedelta
import os
ancho = 150

try:
    print("--Para empezar con el temporizador, llena la informacion!")
    print("Para detener el temporizador, Precione Ctrl + C")
    dia=int(input("Dia-> "))
    mes=int(input("Mes->"))
    ano=int(input("Ano-> "))
    hora=int(input("Hora->"))
    minuto=int(input("Minuto->"))
    segundo=int(input("Segundo->"))

    while True:
        fecha_evento = datetime(ano,mes,dia,hora,minuto,segundo)
        fecha_actual = datetime.now()
        tiempo_restante = fecha_evento - fecha_actual

        if tiempo_restante.total_seconds() <=0:
            os.system("cls")
            print("--YA EL EVENTO COMENZO--")
            break

        dias = tiempo_restante.days
        segundos = tiempo_restante.seconds

        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos = segundos % 60

        os.system("cls")

        print(f"------Tiempo restante para el evento:-------".center(ancho))
        print(f"Tiempo restante: {dias} días | {horas} horas |".center(ancho))
        print((f"{minutos} minutos | {segundos} segundos").center(ancho))
        time.sleep(1)

except ValueError:
    print("Error: Por favor ingrese valores validos:")

except KeyboardInterrupt:
    print("Temporizador culminado")
