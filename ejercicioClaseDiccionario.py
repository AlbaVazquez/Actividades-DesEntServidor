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

#conseguir una lista con todos los nombres y otra con todas las valoraciones
    

