#Construir un programa que tome un numero inicial y cuente hasta 0 mostrando cada numero con un retraso de un segundo
import time
numero = int(input("Digite el numero para comenzar la cuenta: "))

for i in range(numero,-1,-1):
    print(i)
    time.sleep(1)
