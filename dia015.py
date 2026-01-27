#Aplicación de visualización de recetas
import os
def menu():
    os.system("cls")
    print("""Menu de opciones:"
1- Buscar la receta por nombre
2- Ver todas las recetas
3- Salir""")
    

Recetas= {}
def buscar_recetas():
    os.system("cls")

    recetas=[]
    with open("recipesdia15.txt", "r") as file:
        lineas = file.readlines()
        print("Digite el nombre de la receta que desea buscar")
        for linea in lineas:
            linea = linea.strip()
            if not linea.startswith("Instructions") and not linea.startswith("Ingredients"):
                print(linea)
                recetas.append(linea)
        nombre_receta = input("-> ")

        if nombre_receta in recetas:
            encontrado = False
            for linea in lineas:
                linea = linea.strip()
                if nombre_receta == linea:
                    print(linea)
                    encontrado = True
                    continue
                if encontrado:
                    print(linea)
                    if linea.startswith("Instructions"):
                        break
        else:
            print("La receta no se encuentra en el recetario")  

        
def ver_recetas():
    os.system("cls")
    with open("recipesdia15.txt", "r") as file:
        for linea in file.readlines():
            print(linea.strip())

def salir():
    os.system("cls")
    while True:
        try:
            respuesta = int(input("Seguro desea salir del programa? (1- Si, 2- No): "))
            if respuesta == 1:
                print("Vuelva pronto!")
                exit()
            elif respuesta == 2:
                print("Sigamos entonces...")
                break
        except ValueError:
            print("Digite un numero valido= 1 o 2")
            


while True:
    menu()
    try: 
        opcion = int(input("Escriba el numero de la accion que desea hacer: (3 PARA SALIR)"))
    except ValueError:
        print("Por favor ingresar un numero")
        continue
    if opcion < 1 or opcion > 3:
        print("Por favor ingrese un numero dentro del rango (1-3)")

    match(opcion):
        case 1:
            buscar_recetas()    
            input("Presione ENTER para continuar...")

        case 2:
            os.system("cls")
            ver_recetas()
            input("Presione ENTER para continuar...")

        case 3:
            os.system("cls")
            salir()
            
