def sacar_las_calificaciones():
    while True:
        entrada = input("Digite las calificaciones separadas por comas: ")

        try:
       
            notas = [int(nota.strip()) for nota in entrada.split(",")]
            return notas
        except ValueError:
            print(" Solo se permiten numeros enteros")



calificaciones = sacar_las_calificaciones()


resultado_letras = [
    "A" if n >= 90 else
    "B" if n >= 80 else
    "C" if n >= 70 else
    "F"
    for n in calificaciones
]


aprobados = [n for n in calificaciones if n >= 70]
reprobados = [n for n in calificaciones if n < 70]

print("Estudiantes:")

numero_estudiante = 1

for nota in calificaciones:
    letra = resultado_letras[numero_estudiante - 1]

    print("Estudiante", numero_estudiante)
    print("  Nota:", nota)
    print("  Calificación literal:", letra)
    numero_estudiante += 1

print("Aprobados:")
print(aprobados)

print("Reprobados:")
print(reprobados)

print("Resumen final:")
print("Total de estudiantes:", len(calificaciones))
print("Cantidad de aprobados:", len(aprobados))
print("Cantidad de reprobados:", len(reprobados))

