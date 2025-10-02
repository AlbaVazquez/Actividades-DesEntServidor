#!/usr/bin/env python

videoJuegos=[]
listaNombreJuegos=[]
listaValoraciones=[]
total=0
media=0
numVideoJuegos=int(input("¿Cuantos números de video juegos vas a introducir?: "))
for i in range(numVideoJuegos):
    nombre=input("Nombre del videojuego: ")
    valoracion=int(input("Valoración: "))
    categoria=input("Categoria: ")
    videoJuego={"Nombre":nombre,"Valoracion":valoracion,"Categoria":categoria}
    videoJuegos.append(videoJuego)
print(videoJuegos)

listaNombreJuegos=[juego["Nombre"]for juego in videoJuegos] #recorre cada juego dentro de videojuego y accede al valor asociado a la clave nombre
listaValoraciones=[juego["Valoracion"]for juego in videoJuegos]

media=sum([juego["Valoracion"]for juego in videoJuegos])/len(videoJuegos)#se podia haber hecho tambien media=sum(listaValoracion)/len(listaValoraciones)

print(listaNombreJuegos)
print(listaValoraciones)
print(media)