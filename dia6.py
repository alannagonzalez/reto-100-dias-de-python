#Hacer un juego de preguntas de matematicas, con funciones.
import random
import os
import time


def generador_de_preguntas(puntos):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operador = random.choice(['+', '-', '*'])

    if operador == '+':
        respuesta_correcta = num1 + num2

    elif operador == '-':
        respuesta_correcta = num1 - num2

    if operador == '*':
        respuesta_correcta = num1 * num2

    respuesta_del_usuario =int(input(f"Digite el resultado de este problema: {num1} {operador} {num2} = "))

    
    if respuesta_del_usuario == respuesta_correcta:
        puntos += 1
    return puntos

puntos=0

for i in range(1,4):
    os.system("cls")
    print("Empecemos a calcular en...!")
    print("------------------------")
    print(i)
    time.sleep(1)
    os.system("cls")

for i in range(10):
    puntos=generador_de_preguntas(puntos)
    print(f"Cantidad de puntos acumulados: {puntos}/10")
   








