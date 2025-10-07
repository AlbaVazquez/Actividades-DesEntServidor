fichero = open("/home/alumno/Documentos/ejemplo.txt", "w")
fichero.writelines(["Hola", "Adios"])

fichero = open("/home/alumno/Documentos/ejemplo.txt", "r")
print(fichero.read())
fichero.close()

with open("/home/alumno/Documentos/ejemplo.txt", "r") as fichero:
    for linea in fichero:
        print(linea)
# El fichero se cierra automaticamente al salir del bloque with


import csv

ficherocsv = open("/home/alumno/Documentos/ejemplo.csv", "w")
contenido = csv.writer(ficherocsv)
contenido.writerow(["Alba", "Vázquez", "19"])

ficherocsv = open("/home/alumno/Documentos/ejemplo.csv", "r")
contenido = csv.reader(ficherocsv)
print(list(contenido))
ficherocsv.close()

with open("/home/alumno/Documentos/ejemplo.csv", "r") as ficherocsv:
    contenido = csv.reader(ficherocsv)
    for fila in contenido:
        print(fila)
        
        
import json

datos = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
ficherojson = open("/home/alumno/Documentos/ejemplo.json", "w")
json.dump(datos,ficherojson)
ficherojson.close()

with open("/home/alumno/Documentos/ejemplo.json") as ficherojson:
    datos = json.load(ficherojson)
    print(datos)