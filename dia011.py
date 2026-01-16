import os

def menu_interactivo():
    print("MENU DE OPCIONES:")
    print("-----------------")
    print("""1-Suma
2-Resta
3-Multiplicacion
4-Division
5-Salir""")    

def suma():
    while True:
     try:
       num1 = int(input("Digite el numero 1: "))
       break
     except ValueError:
       print("SOLO NUMEROS")
       
    while True:
     try:
        num2 = int(input("Digite el numero 2: "))
        break
     except ValueError:
          print("SOLO NUMEROS")

    print(f"La suma de estos digitos es: {num1 + num2}")
    input("Precione enter para volver al menu")

def resta():
    while True:
        try:
            num1 = int(input("Digite el numero 1: "))
            break
        except ValueError:
            print("SOLO NUMEROS")
        
    while True:
        try:
            num2 = int(input("Digite el numero 2: "))
            break
        except ValueError:
            print("SOLO NUMEROS")

    print(f"La resta de estos digitos es: {num1 - num2}")
    input("Precione enter para volver al menu")



def multiplicacion():
    while True:
     try:
       num1 = int(input("Digite el numero 1: "))
       break
     except ValueError:
       print("SOLO NUMEROS")
       
    while True:
     try:
        num2 = int(input("Digite el numero 2: "))
        break
     except ValueError:
          print("SOLO NUMEROS")

    print(f"La multiplicacion de estos digitos es: {num1 * num2}")
    input("Precione enter para volver al menu")


def division():
    while True:
        try:
            num1 = int(input("Digite el numero 1: "))
            break
        except ValueError:
           print("Valor invalido")

    while True:
     try:
        num2 = int(input("Digite el numero 2: "))
        print(f"La Division de estos digitos es: {num1 / num2}")
        break
       
     except ValueError:
          print("SOLO NUMEROS")

     except ZeroDivisionError:
        print("No se puede dividir entre 0")
        
    


def salir():
   print("Vuelva pronto!")



while True: 
   menu_interactivo()
   try:
        opcion = int(input("Seleccione la operacion que desea hacer (1-5)"))   
   except ValueError:
        print("VALOR INVALIDO")
        continue

   if opcion < 1 or opcion > 5:
        print("Recuerde elegir un numero del 1 al 5: ")
        continue
      

   match(opcion):
        case 1:
            os.system("cls")
            suma()
            input("Precione enter para volver al menu")

        case 2:
            os.system("cls")
            resta()
            input("Precione enter para volver al menu")

        case 3:
            os.system("cls")
            multiplicacion()
            input("Precione enter para volver al menu")

        case 4:
            os.system("cls")
            division()
            input("Precione enter para volver al menu")

        case 5:
            os.system("cls")
            salir()
            break

         
          

