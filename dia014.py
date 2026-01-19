import random
import string

def pedir_longitud():
    while True:
        try:
            contrasena_longitud = int(input("Digite la longitud de la contraseña, minimo 4 caracteres:"))
            if contrasena_longitud < 4:
                print("Mayor a 4")
            else:
                return contrasena_longitud
        except ValueError:
            print("Solo numeros")


def generado_contrasena(longitud):
    letras_mayusculas = list(string.ascii_uppercase)
    letras_minusculas =list(string.ascii_lowercase)
    numeros =list(string.digits)
    caracteres=["/", "$", "*", "#"]

    caracteres_unidos = letras_mayusculas+letras_minusculas+numeros+caracteres
    contrasena_final=[]
    for _ in range(longitud):
        contrasena_final.append(random.choice(caracteres_unidos))
    contrasena_final = "".join(contrasena_final)
    return contrasena_final


print("BIENVENIDO A TU GENERADOR DE CONTRASEÑA:")
print(generado_contrasena(pedir_longitud()))

