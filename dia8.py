import os
"""Crear una agenda de contactos que permita
Agregar contactos
Buscar por nombre
Ver todos los contactos
editar la informacion de un contacto
eliminar un contacto
salir"""


contactos = []

def mostrar_menu():
    os.system("cls") 
    print("""
1-Agregar contactos
2-Buscar por nombre
3-Ver todos los contactos
4-editar la informacion de un contacto
5-eliminar un contacto
6-salir""")


def agregar_contacto(contactos):
    os.system("cls")
    nombre = input("Digite el nombre del contacto: ").strip()
    numero = input("Digite el numero: ").strip()
    correo = input("Digite el correo correspondiente: ").strip()

    contactos.append({"nombre":nombre, "numero": numero,"correo":correo})
    print("Contacto agregado correctamente")


def buscar_pornombre(contactos):
     os.system("cls")
     nombre_buscar = input(("Digite el nombre del contacto para extraer informacion: "))
     for contacto in contactos:
        if nombre_buscar == contacto["nombre"]:
            print(f"nombre: {contacto["nombre"]}")
            print(f"numero: {contacto["numero"]}")
            print(f"correo: {contacto["correo"]}")

def ver_los_contactos(contactos):
    print(f"Lista de contactos:") 
    if not contactos:
        print("Aun no hay contactos")

    for contacto in contactos:
        print(f"nombre: {contacto["nombre"]}")
        print(f"numero: {contacto["numero"]}")
        print(f"correo: {contacto["correo"]}")
       

def editar_contactos(contactos):
    os.system("cls")
    nombre_a_encontrar = input("Digite el nombre del usuario que desea editar: ").strip()
    for contacto in contactos:
        if nombre_a_encontrar == contacto["nombre"]:
            print("1-Editar nombre")
            print("2- Editar numero")
            print("3- Editar correo")
            opcion = input("Seleccione lo que desea hacer: ")

            if opcion == "1":
                contacto["nombre"] = input("Digite el nuevo nombre: ").strip()
            elif opcion == "2":
                contacto["numero"] = input("Digite el nuevo numero").strip()
            elif opcion == "3": 
                contacto["correo"] = input("Digite el nuevo correo").strip()  
            else:
                print("Opcion invalida")  
                return

            print ("Contacto editado correctamente")
            return        


def eliminar_contacto(contactos):
    os.system("cls")
    nombre_eliminar = input("Digite el nombre del contacto a eliminar: ").strip()

    for contacto in contactos:
        if contacto["nombre"] == nombre_eliminar:
            contactos.remove(contacto)
            print("Contacto eliminado correctamente")
            return

def salir_del_programa():
    os.system("cls")
    print("Saliendo de contactos")


while True:
    mostrar_menu()
    print("*******************************************************")
    opcion_menu = input("""Seleccione el numero de acuero a lo que desea hacer hoy 
    --> """)
    print("")

    match opcion_menu:
        case "1":
            agregar_contacto(contactos)
            input("Precione enter")
            
        case "2":
            buscar_pornombre(contactos)
            input("Precione enter")

        case "3":
            ver_los_contactos(contactos)
            input("Precione enter")

        case "4":
            editar_contactos(contactos)
            input("Precione enter")

        case "5":  
            eliminar_contacto(contactos) 
            input("Precione enter")

        case "6":
            salir_del_programa() 
            input("Precione enter")     
            break

