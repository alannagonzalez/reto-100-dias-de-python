#Haz un programa que pida al usuario dos numeros y diga cual es mayor, si son iguales, o son iguales a 0
num1=int(input("Digite el primer numero: "))
num2=int(input("Digite el segundo numero: "))

if num1 > num2:
    print(f"{num1} es mayor a {num2}")

elif num2 > num1:
    print(f"{num2} es mayor a {num1}")

else:
     print(f"{num2} es igual a {num1}")     

if num1 == 0:
   print("El primer numero es igual a 0")

if num2 == 0:
   print("El segundo numero es igual a 0")

 