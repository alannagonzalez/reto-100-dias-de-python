#Hacer un generador de informes estudiantiles, primero leer las calificaciones desde un csv,
#Calcular la calificacion promedio de cada estudiante, identificar los estudiantes con mejor nota
#escribir los datos procesados en un nuevo archivo csv (promedio y estatus de cada estudiante)

import csv
def generador_informes(entrada, salida):
    with open(salida, "w", newline= "") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre", "matematicas","ingles","sociales","naturales","promedio","estatus"])
    with open (entrada, "r") as file:
        reader = csv.DictReader(file)
        for linea in reader:
         
            promedio = (float(linea["matematicas"]) + float(linea["ingles"]) + float(linea["sociales"]) + float(linea["naturales"])) / 4
            if promedio >= 70:
                estatus = "Pasa"
            else:
                estatus = "Repite"

            with open(salida, "a", newline= "") as archivo:
                writer = csv.writer(archivo)
                writer.writerow([linea["nombre"],linea["matematicas"],linea["ingles"], linea["sociales"],linea["naturales"], promedio,estatus])


generador_informes("estudiantesdia17.csv","resultadofinaldia17.csv")

