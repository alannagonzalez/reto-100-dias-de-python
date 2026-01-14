import os

INGREDIENTES = {"pasta", "salsa", "sal", "ajo", "tomate", "cebolla", "sopita", "aceite", "agua"}
    

def mostrar_menu():
    print("""Digite un numero del 1 al 4 para la accion que desee
1: Escribir ingredientes
2: Ver ingredientes de la pasta
3: Resultado de mis ingredientes 
4: Salir del programa""")


ingredientes_usuario = set()  
def pedir_ingredientes():   
    print("Digite uno por uno los ingredientes que tiene para la pasta: (Escriba Exit para salir)")
    while True:
        ingrediente_pedido = input("--> """).strip().lower()
        if ingrediente_pedido == "exit":
            break
        else:
            ingredientes_usuario.add(ingrediente_pedido)

def mostrar_ingredientes(ingredientes_usuario):
    print("LISTA DE INGREDIENTES")
    for ingrediente in INGREDIENTES:
        if ingrediente in ingredientes_usuario:
            print(f"{ingrediente}:, Lo tienes")
        else:
            print(f"{ingrediente}")

def identificar_ingredientes():
    ingre_faltantes = INGREDIENTES - ingredientes_usuario
    ingre_extras = ingredientes_usuario - INGREDIENTES

    if ingre_faltantes and ingre_extras:
        print("Ingredientes faltantes: ", ingre_faltantes)
        print("Ingredientes extras:", ingre_extras)

    elif ingre_faltantes:
        print("Ingredientes faltantes:", ingre_faltantes)

    elif ingre_extras:    
        print("Ingredientes extras:", ingre_extras)
        print("Todos los ingredientes estan en la receta")
    else:
        print("Todos los ingredientes estan correctos!, list@ para cocinar?")


while True: 
    os.system("cls")
    mostrar_menu()
    opcion = input("--> ")
    os.system("cls")

    match opcion:
        case "1":
            pedir_ingredientes()
        case "2": 
            mostrar_ingredientes(ingredientes_usuario)
        case "3": 
            identificar_ingredientes()
        case "4": 
            break
        
    input("Pulse enter")

    









