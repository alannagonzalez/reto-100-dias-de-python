import os

"""Permitir agregar 
ver todas las notas"""


def menu():
    print("""---MENU DE OPCIONES:
1-Agregar diario
2-Ver diarios
3-Buscar diario por palabra
4-Salir""")
    
def anadir_diario():
    while True:
        os.system("cls")
        print("Digite el diario: (EXIT PARA SALIR)")
        diario = input("--> ").lower()
        if diario == "exit":
            break
        else:
            with open("archidiario.txt", "a") as file:
                file.write(diario+ "\n")


def ver_diarios():
    os.system("cls")
    with open("archidiario.txt", "r") as file:
        for i, note in enumerate(file.readlines(), start =1):
            print(f"{i}.{note}", end ="")


def buscar_por_palabra():
    palabra = input("Digite la palabra para empezar a buscar: ").lower()
    with open("archidiario.txt", "r") as file:
        for linea in file:
            if palabra in linea.lower():
                print("Diario encontrado: \n",linea)


while True: 
   menu()
   try:
        opcion = int(input("Seleccione la operacion que desea hacer (1-4)"))   
   except ValueError:
        print("VALOR INVALIDO")
        continue

   if opcion < 1 or opcion > 4:
        print("Recuerde elegir un numero del 1 al 4: ")
        continue
      

   match(opcion):
        case 1:
            os.system("cls")
            anadir_diario()
            input("Precione enter para volver al menu")

        case 2:
            os.system("cls")
            ver_diarios()
            input("Precione enter para volver al menu")

        case 3:
            os.system("cls")
            buscar_por_palabra()
            input("Precione enter para volver al menu")

        case 4:
            os.system("cls")
            print("Pase feliz dia")
            break    
    



 










        