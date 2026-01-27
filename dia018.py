#Hacer una mini aplicacion de tareas que permita ver todas las tareas, agregar tareas, actualizar el estado de una tarea
#eliminar tarea y salir del programa.
import os
import json

def menu():
    print("""---MENU DE OPCIONES:
1- Ver todas las tareas
2- Agregar tarea
3- Actualizar tarea
4- Estado de la tarea
5- Eliminar tarea
6- Salir""")
     

def ver_tareas():
    with open("tareas018.json", "r") as file:
        tareas = json.load(file)
        for linea in tareas:
            print(linea)


def agregar_tareas():
    with open("tareas018.json", "r") as file:
        tareas = json.load(file)
    nueva_tarea = input("Ingrese la nueva tarea: ")
    tareas.append({"tarea": nueva_tarea, "estado": "pendiente"})
    with open("tareas018.json", "w") as file:
        json.dump(tareas, file)
        

def actualizar_tareas():
     with open("tareas018.json", "r") as file:
        tareas = json.load(file)
        for linea in enumerate(tareas, start=1):
            print(linea)
        num_tarea = int(input("Digite el numero de la tarea que desea actualizar: "))
        nuevo_estado = input("Digite el nuevo estado de la tarea (pendiente/completada): ").lower()
        if nuevo_estado in ["pendiente", "completada"]:
            tareas[num_tarea - 1]["estado"] = nuevo_estado
            with open("tareas018.json", "w") as file:
                json.dump(tareas, file)     


def estado_de_la_tarea():
    with open("tareas018.json", "r") as file:
        tareas = json.load(file)
        for linea in enumerate(tareas, start=1):
            print(linea)
        num_tarea = int(input("Digite el numero de la tarea para ver su estado: "))
        print(f"El estado de la tarea '{tareas[num_tarea - 1]['tarea']}' es: {tareas[num_tarea - 1]['estado']}")

def eliminar_tarea():
    with open("tareas018.json", "r") as file:
        tareas = json.load(file)
        for linea in enumerate(tareas, start=1):
            print(linea)
        num_tarea = int(input("Digite el numero de la tarea que desea eliminar: "))
        tareas.pop(num_tarea - 1)
        with open("tareas018.json", "w") as file:
            json.dump(tareas, file)

while True: 
   menu()
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
            ver_tareas()
            input("Precione enter para volver al menu")

        case 2:
            os.system("cls")
            agregar_tareas()
            input("Precione enter para volver al menu")

        case 3:
            os.system("cls")
            actualizar_tareas
            input("Precione enter para volver al menu")

        case 4:
            os.system("cls")
            estado_de_la_tarea()
             
        case 5:
            os.system("cls")
            eliminar_tarea()
        
        case 6:
            os.system("cls")
            print("Pase feliz dia")
            break
           
