from statistics import median


Juegos = ["The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey", "Minecraft", "Genshin Impact", "Animal Crossing" ]
Valoraciones = []
vPositivas = 0
posMax = 0
posMin = 0
vMax = 0
vMin = 10

for i in range (len(Juegos)):
    valoracion = int(input("Valoración para " + Juegos[i] + ": "))
    
    if valoracion > vMax:
        posMax = i
        vMax = valoracion
        
    if valoracion < vMin:
        posMin = i
        vMin = valoracion
    
    if valoracion >= 8:
        vPositivas = vPositivas + 1
        
    if valoracion >= 1 and valoracion <= 10:
        Valoraciones.append(valoracion)
    else:
       print("Su valoración debe de ser de 1 a 10.")

    
print("\n VALORACIONES --------------------")
for i in range(0, len(Juegos)):
    print(Juegos[i], " --- Valoración: ", Valoraciones[i])
    
print("Media de valoraciones: ", median(Valoraciones))
print("Valoraciones mayores o iguales a 8: ", vPositivas)
print("Mejor valoración: ", Juegos[posMax], " --- ", vMax)
print("Peor valoración: ", Juegos[posMin], " --- ", vMin)

     
    