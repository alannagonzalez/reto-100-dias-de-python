#Aplicacion para una lista de compras que permita ver, agregar, eliminar productos, limpiar lista y una opcion para salir
import os
def menu():
    print("-----MENU DE LISTA-----")
    print("1-Agregar articulo")
    print("2-Eliminar articulo")
    print("3-Ver lista")
    print("4-Limpiar lista")
    print("5-Salir de la app")
    print("----------------------")
    print("")

lista_compra = []
while True:
    menu()
    try:
      
        opcion_menu = int(input("Bienvenido!, seleccione la opcion correspondiente a lo que desee (1-5): "))
    except:
        print("DIGITE UN UN NUMERO(1-5)")
    
    if opcion_menu == 1:
        agregar = input("Que desea agregar en la lista de compras?: ")
        lista_compra.append(agregar)

    if opcion_menu == 2:
        if not lista_compra:
            print("Su lista esta vacia, no puede eliminar nada")

        else:
            eliminar = int(input("Escriba el indice del articulo que desea eliminar:"))
            lista_compra.pop(eliminar)

    if opcion_menu == 3:
        for cuenta, articulo in enumerate(lista_compra):
            print(cuenta+1, articulo)
        input("Precione enter")

    if opcion_menu ==4:
        lista_compra.clear()

    if opcion_menu ==5:
        print("Gracias por venir, vuelva pronto!")
        break    






        

