cantidad = int(input("¿Cuántos números quieres meter en la lista?"))

lista = []
lista2 = [7,5,6]

for i in range(cantidad):
    num = int(input("Número:"))
    lista.append(num)
    
print("La lista es:", sorted(lista + lista2))

media = sum(lista) / len(lista)
print ("La media es: ", media)

buscar = int(input("Posición a buscar: "))
# if buscar < len(lista):
#     print("El número en la posición", buscar, "es", lista[buscar])
# else:
#     print("Posición no válida")

num = int(input("Número a buscar: "))
if num in lista:
    print("El número se encuentra en la posición ", lista.index(num))