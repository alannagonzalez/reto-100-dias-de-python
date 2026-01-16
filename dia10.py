import os

def menu():
    print("""---MENU DE OPCIONES:
1-Añadir notas
2-Ver las notas
3-Eliminar notas
4-Salir de la app""")
    
def anadir_nota():
    while True:
        os.system("cls")
        print("Digite la nota: (DIGITE EXIT PARA SALIR)")
        nota = input("--> ").lower()
        if nota == "exit":
            break
        else:
            with open("file.txt", "a") as file:
                file.write(nota+ "\n")

def ver_notas():
    os.system("cls")
    with open("file.txt", "r") as file:
        for i, note in enumerate(file.readlines(), start =1):
            print(f"{i}.{note}", end ="")

def eliminar_notas():
    os.system("cls")
    with open("file.txt","w" ) as file:
        file.write("")



while True:
    menu()
    opcion = input("Digite el numero de la accion que desea realizar:")

    match(opcion):
        case "1":
            anadir_nota()
            input("Pulse enter")
            os.system("cls")
            

        case "2": 
            ver_notas()  
            input("Pulse enter")
            os.system("cls")

        case "3":
            eliminar_notas()
            input("Pulse enter")
            os.system("cls")

        case "4": 
            print("Fin del programa") 
            break  










        