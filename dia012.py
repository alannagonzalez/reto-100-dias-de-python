import os

def menu():
    print("---Menu interactivo---")
    print("""1-Celsius a Fahrenheit1
2-Celsius a Kelvin
3-Fahrenheit a Celsius
4-Fahrenheit a Kelvin
5-Kelvin a Celsius
6-Kelvin a Fahrenheit
7-Salir
------------------------         
          """)

def celsius_Fahrenheit():
    while True:
        try:
            celsius = float(input("Digite los celsius que quiere convertir a Fahrenheit"))
            break
        except ValueError:
            print("SOLO NUMEROS")
    
    return f"{celsius} en Fahrenheit = {(celsius * 9/5) +32}"

def celsius_kelvin():
    while True:
        try:
            celsius = float(input("Digite los celsius que desea convertir a Kelvin"))
            break
        except ValueError:
            print("SOLO NUMEROS")
    return f"{celsius} en Kelvin = {celsius + 273.15}"

def Fahrenheit_Celsius():
    while True:
        try:
            Fahrenheit = float(input("Digite los Fahrenheit que desea convertir a Celsius"))
            break
        except ValueError:
            print("SOLO NUMEROS")
    return f"{Fahrenheit} en Celsius = {(Fahrenheit - 32)* 5/9}"

def Fahrenheit_Kelvin():
    while True:
        try:
            Fahrenheit = float(input("Digite los Fahrenheit que desea convertir a Kelvin"))
            break
        except ValueError:
            print("SOLO NUMEROS")
    return f"{Fahrenheit} en Kelvin = {(Fahrenheit - 32)* 5/9 + 273.15}"
    
   
def Kelvin_Celsius():
    while True:
        try:
            Kelvin = float(input("Digite los Kelvin que desea convertir a Celsius"))
            break
        except ValueError:
            print("SOLO NUMEROS")
    return f"{Kelvin} en Celsius = {Kelvin -273.15}"

def Kelvin_Fahrenheit():  
    while True:
        try:
            Kelvin = float(input("Digite los Kelvin que desea convertir a Fahrenheit"))
            break
        except ValueError:
            print("SOLO NUMEROS")
    return f"{Kelvin} en Fahrenheit = {(Kelvin -273.15)* 9/5 + 32}"

def salir():
    print("Vuelva pronto") 


while True: 
   menu()
   try:
        opcion = int(input("Seleccione la operacion que desea hacer (1-7)"))   
   except ValueError:
        print("VALOR INVALIDO")
        continue

   if opcion < 1 or opcion > 7:
        print("Recuerde elegir un numero del 1 al 7: ")
        continue
      

   match(opcion):
        case 1:
            os.system("cls")
            celsius_Fahrenheit()
            input("Precione enter para volver al menu")

        case 2:
            os.system("cls")
            celsius_kelvin()
            input("Precione enter para volver al menu")

        case 3:
            os.system("cls")
            Fahrenheit_Celsius
            input("Precione enter para volver al menu")

        case 4:
            os.system("cls")
            Fahrenheit_Kelvin
            input("Precione enter para volver al menu")

        case 5:
            os.system("cls")
            Kelvin_Celsius
            input("Precione enter para volver al menu")

        case 6:
            os.system("cls")
            Kelvin_Fahrenheit
            input("Precione enter para volver al menu")

        case 7:
            os.system("cls")
            salir()
            break    
    



