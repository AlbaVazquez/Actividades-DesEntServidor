videojuegos = []
totalV = 0

cantidad = int(input("¿Cuántos videojuegos quieres introducir? "))

for i in range(cantidad):
    nombre = input("Nombre del videojuego: ")
    valoracion = int(input("Valoración del videojuego (1-10): "))
    categoria = input("Categoría del videojuego: ")

    videojuego = {
        "nombre": nombre,
        "valoracion": valoracion,
        "categoria": categoria
    }
    
    videojuegos.append(videojuego)
    
print (videojuegos)

for juego in videojuegos:
    print(juego["nombre"])
    totalV += juego["valoracion"]
    
media = totalV / cantidad
print("La valoración media es:", media)

#conseguir una lista con todos los nombres y otra con todas las valoraciones, calcular la media con 
#la nueva lista de valoraciones. Realizar las listas en una sola línea de código.
listaNombres = [juego["nombre"] for juego in videojuegos]
listaValoraciones = [juego["valoracion"] for juego in videojuegos]
media2 = sum(listaValoraciones) / len(listaValoraciones)

print("Lista de nombres:", listaNombres)
print("Lista de valoraciones:", listaValoraciones)
print("La valoración media calculada con las nuevas listas es:", media2)


