# Dada una lista de cadenas, pide una cadenena por teclado e indica si está 
# en la lista, indica cuantas veces aparece en la lista, lee otra cadena y 
# sustituye la primera por la segunda en la lista, y por último borra la 
# cadena de la lista

lista = ['leche', 'tomates', 'galletas', 'filetes', 'leche']

cadena = input("Indica una cadena: ")

if cadena in lista:
    print("La cadena", cadena, " está en la lista")
else: 
    print("La cadena no está en la lista")
    
print("La cadena aparece: ", lista.count(cadena), " veces")

cadena2 = input("Indica otra cadena: ")
apariciones = lista.count(cadena)
pos = 0
for i in range(0, apariciones):
    pos = lista.index(cadena, pos)
    lista[pos] = cadena2
print(lista)



# Dado una lista, hacer un programa que indique si está ordenada o no.

lista = [1,2,3,4]

if lista == sorted(lista):
    print("La lista está ordenada: ", lista)
else: 
    print("La lista no está ordenada: ", lista)
    


#Lee por teclado números y guardalo en una lista, el proceso finaliza 
#cuando metamos un número negativo. Muestra el máximo de los números 
#guardado en la lista, muestra los números pares.

num = int(0)
lista = []

while num >= 0: 
    num = int(input("Número: "))
    #Necesito declarar esta condición para que no me añada el número negativo a la lista
    if num >= 0:
        lista.append(num)

print("El número máximo es: ", max(lista))

pares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)

print("Los números pares: ", pares)



# Realizar un programa que, dada una lista, devuelva una nueva lista cuyo
# contenido sea igual a la original pero invertida. Así, dada la lista
# [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’,
# ‘buen’, ‘Di’].

lista = ['Esto', 'es', 'una', 'frase']
lista.reverse
print(lista)

print(lista[::-1])