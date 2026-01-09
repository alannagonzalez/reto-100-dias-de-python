#Administrador de tareas:
import os
def mostrar_menu():
    print("""*******************************************************
1-Agregar tareas
2-Ver todas las tareas
3-Marcar una tarea como completada
4-Eliminar una tarea
5-Salir del programa""")
    
lista_tareas = []
def ver_tareas(lista_tareas):
    for cuenta, tarea in enumerate(lista_tareas):
        print(cuenta+1, tarea)


def agregar_tarea(lista_tareas):
    while True:
        tarea_agregada = input("""Digite la tarea que desea agregar:
--> """).strip()

        if tarea_agregada.replace(" ", "").isalpha():
            lista_tareas.append(tarea_agregada)
            print("Tarea agregada correctamente")
            break
        else:
            print(" Solo letras, no numeros ni espacios ")

def marcar_tarea_completada(lista_tareas):
    ver_tareas(lista_tareas)
    while True:
        try:

            tarea_para_marcar = int(input("""Digite el numero de la tarea completada: 
                                        --> """))
            if tarea_para_marcar >= 1 and tarea_para_marcar <= len(lista_tareas):
                lista_tareas[tarea_para_marcar -1] = "-> Completada" + lista_tareas[tarea_para_marcar - 1]
            else:
                print("Numero fuera de rango")
        except:
            print("Digite solo numeros por favor")
 
        
    
   
    

#BLOQUE LIMPIO
while True:
    nombre_usuario = input("""Digite su nombre para una experiencia mas personal
--> """).strip()
    if nombre_usuario.isalpha():
        break
    else:
        print("Los numeros no estan permitidos, DIGITE SU NOMBRE")


os.system("cls")
print(f"----Bienvenid@ {nombre_usuario}----")
mostrar_menu()
print("*******************************************************")
while True:
    try:
        opcion_menu = int(input("""Seleccione el numero de acuero a lo que desea hacer hoy 
        --> """))
        print("")
        break

    except:
        print("NO LETRAS, SOLO NUMEROS")

match opcion_menu:
    case 1:
        agregar_tarea(lista_tareas)

    case 2:
        if not lista_tareas:
            print("Su lista de tareas esta vacia")
        else:    
            ver_tareas(lista_tareas)

    case 3:

    case 4:

    case 5:        


